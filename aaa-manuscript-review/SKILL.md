---
name: aaa-manuscript-review
description: >
  Review academic manuscripts for compliance with AAA (American Accounting
  Association) / The Accounting Review (TAR) submission guidelines. Applies
  tracked changes (Word redline via w:del/w:ins XML) to mark every violation
  found, and returns a compliance checklist. Works on .docx files.
---

# AAA/TAR Manuscript Review Skill

## Overview

This skill reviews a Word (.docx) manuscript against the official AAA/TAR
preparation guidelines and applies **tracked changes** directly to the document
so the author can accept or reject each correction. A compliance checklist is
also produced.

## Workflow

### Step 1 — Obtain the manuscript

If the user provides a file path, use it directly.
Output file: same directory, same name with ` - REVIEWED` appended before `.docx`.

### Step 2 — Unpack the docx

```bash
python ~/.claude/skills/docx/scripts/office/unpack.py "<input.docx>" "<workspace_dir>"
```

`<workspace_dir>` should be a temporary directory, e.g. a subfolder of the
manuscript's directory named `_review_workspace`.

> If `unpack.py` fails with `TypeError: unsupported operand type(s) for |`
> (Python 3.9), patch it:
> ```bash
> sed 's/ | None//g' ~/.claude/skills/docx/scripts/office/unpack.py > /tmp/unpack_compat.py
> python /tmp/unpack_compat.py "<input.docx>" "<workspace_dir>"
> ```
> Apply the same `sed` fix to `pack.py` when repacking.

### Step 3 — Extract and analyse text

Parse `<workspace_dir>/word/document.xml` with lxml.
For each paragraph, collect the visible text (runs NOT inside `w:del` elements).
Check every rule in `references/aaa_guidelines.md` systematically.

Key extraction helpers (Python / lxml):

```python
from lxml import etree
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
def wt(tag): return f"{{{W}}}{tag}"

def visible_text(para):
    parts = []
    for child in para:
        tag = etree.QName(child.tag).localname
        if tag == "r":
            parts.append("".join(t.text or "" for t in child.findall(wt("t"))))
        elif tag == "ins":
            for r in child.findall(wt("r")):
                parts.append("".join(t.text or "" for t in r.findall(wt("t"))))
    return "".join(parts)
```

### Step 4 — Apply tracked changes

For every violation, apply a `w:del` / `w:ins` pair using author `"AAA-TAR Review"`
and date `"<today>T00:00:00Z"`.

**Run-level substitution** (for in-place text changes):

```python
import copy, re

def replace_in_run(para, run_el, old_sub, new_sub, change_id, author, date):
    """Split a run and wrap old_sub in w:del, new_sub in w:ins."""
    full = "".join(t.text or "" for t in run_el.findall(wt("t")))
    idx = full.find(old_sub)
    if idx == -1:
        return False
    parent = run_el.getparent()
    pos = list(parent).index(run_el)
    parent.remove(run_el)
    ip = pos
    if idx > 0:
        r_before = copy.deepcopy(run_el)
        for t in r_before.findall(wt("t")): t.text = full[:idx]
        parent.insert(ip, r_before); ip += 1
    # del
    d = etree.Element(wt("del"))
    d.set(wt("id"), str(change_id)); d.set(wt("author"), author); d.set(wt("date"), date)
    rd = copy.deepcopy(run_el)
    for t in rd.findall(wt("t")): t.tag = wt("delText"); t.text = old_sub
    d.append(rd); parent.insert(ip, d); ip += 1
    # ins
    i = etree.Element(wt("ins"))
    i.set(wt("id"), str(change_id+1)); i.set(wt("author"), author); i.set(wt("date"), date)
    ri = copy.deepcopy(run_el)
    for t in ri.findall(wt("t")):
        t.text = new_sub
        if " " in new_sub: t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    i.append(ri); parent.insert(ip, i); ip += 1
    if full[idx+len(old_sub):]:
        r_after = copy.deepcopy(run_el)
        for t in r_after.findall(wt("t")): t.text = full[idx+len(old_sub):]
        parent.insert(ip, r_after)
    return True
```

**Whole-paragraph replacement** (for reference list reformatting):

```python
def replace_para_tracked(para, new_text, change_id, author, date):
    old_runs = para.findall(wt("r"))
    if not old_runs: return False
    old_text = "".join("".join(t.text or "" for t in r.findall(wt("t"))) for r in old_runs)
    if old_text.strip() == new_text.strip(): return False
    rpr = old_runs[0].find(wt("rPr"))
    ppr = para.find(wt("pPr"))
    ip = (list(para).index(ppr) + 1) if ppr is not None else 0
    for r in old_runs: para.remove(r)
    # del
    d = etree.Element(wt("del"))
    d.set(wt("id"), str(change_id)); d.set(wt("author"), author); d.set(wt("date"), date)
    rd = etree.SubElement(d, wt("r"))
    if rpr is not None: rd.append(copy.deepcopy(rpr))
    dt = etree.SubElement(rd, wt("delText")); dt.text = old_text
    dt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    para.insert(ip, d)
    # ins
    ins = etree.Element(wt("ins"))
    ins.set(wt("id"), str(change_id+1)); ins.set(wt("author"), author); ins.set(wt("date"), date)
    ri = etree.SubElement(ins, wt("r"))
    if rpr is not None: ri.append(copy.deepcopy(rpr))
    it = etree.SubElement(ri, wt("t")); it.text = new_text
    it.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    para.insert(ip+1, ins)
    return True
```

**Adding Word comments** (for structural issues like missing AI disclosure):

```python
def add_comment(para, run_el, comment_text, comm_id):
    cs = etree.Element(wt("commentRangeStart")); cs.set(wt("id"), comm_id)
    ce = etree.Element(wt("commentRangeEnd")); ce.set(wt("id"), comm_id)
    pos = list(para).index(run_el)
    para.remove(run_el)
    para.insert(pos, cs); para.insert(pos+1, run_el); para.insert(pos+2, ce)
    ref_run = etree.Element(wt("r"))
    rpr2 = etree.SubElement(ref_run, wt("rPr"))
    etree.SubElement(rpr2, wt("rStyle")).set(wt("val"), "CommentReference")
    cr = etree.SubElement(ref_run, wt("commentReference")); cr.set(wt("id"), comm_id)
    para.insert(pos+3, ref_run)
    # Also add to comments.xml (see Step 5)
```

### Step 5 — Write comments.xml and relationships

If any Word comments were added, ensure:
1. `word/comments.xml` exists with all `w:comment` elements
2. `word/_rels/document.xml.rels` has the comments relationship
3. `[Content_Types].xml` has the comments content type override

### Step 6 — Repack

```bash
SKILLS=~/.claude/skills
sed 's/ | None//g' "$SKILLS/docx/scripts/office/pack.py" > /tmp/pack_compat.py
PYTHONUTF8=1 PYTHONPATH="$SKILLS/docx/scripts/office" \
    python /tmp/pack_compat.py "<workspace_dir>" "<output.docx>"
```

### Step 7 — Produce compliance checklist

After saving the reviewed docx, output a Markdown checklist:

```
# AAA/TAR Compliance Review — <manuscript title>

## Violations Found (Tracked Changes Applied)
- [ ] §4 Numbers: "10" → "ten" in body text (N instances)
- [ ] §5 Percentages: "%" → "percent" in body text (N instances)
- [ ] §7 Citations: "& Author" → "and Author" in in-text citation
- [ ] §8 References: Full list reformatted APA → TAR (N entries)
- [ ] §AI: AI Disclosure statement missing (comment added)

## Issues Requiring Manual Review
- [ ] §2 Anonymous review: author names visible on title page
- [ ] §8 References: Verify reformatted entries, especially entries with Jr./Sr.
  suffixes or non-standard author names

## Items That Passed
- [x] Section heading levels and format
- [x] No "N/A" in tables (should be "NA")
- [x] In-text citation year format (no comma before year)
- [x] Gender-neutral language
```

---

## Rules Reference

See `references/aaa_guidelines.md` for the full rule set.

## Important Caveats

- The reference list reformatter handles standard cases well but may need manual
  correction for: authors with Jr./Sr./II suffixes, corporate/institutional authors,
  entries already partially in TAR format.
- Percentages in parenthetical statistical contexts (e.g., `88.1% (88.3%)`) are
  changed to `percent` per TAR rules, but the author may verify each one.
- Tracked changes are authored as `"AAA-TAR Review"` so they are easy to filter
  in Word's reviewing pane.
- This skill does NOT check page count, font, margins, or line spacing — those
  require visual inspection.
