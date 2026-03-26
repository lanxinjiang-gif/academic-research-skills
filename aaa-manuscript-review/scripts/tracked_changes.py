"""
Tracked-change helpers for AAA/TAR manuscript review.
Usage: import from a review script; call the helpers directly.
"""
import copy
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XS = "http://www.w3.org/XML/1998/namespace"

def wt(tag):  return f"{{{W}}}{tag}"
def xs(attr): return f"{{{XS}}}{attr}"

_id_counter = [5000]

def next_id():
    _id_counter[0] += 1
    return _id_counter[0]

def run_text(r):
    return "".join((t.text or "") for t in r.findall(wt("t")))

def visible_text(para):
    """Return visible text of a paragraph (excludes w:del content)."""
    parts = []
    for child in para:
        tag = etree.QName(child.tag).localname
        if tag == "r":
            parts.append(run_text(child))
        elif tag == "ins":
            for r in child.findall(wt("r")):
                parts.append(run_text(r))
    return "".join(parts)

def _clone_run(run_el, text):
    r2 = copy.deepcopy(run_el)
    for t in r2.findall(wt("t")):
        t.text = text
        if " " in text:
            t.set(xs("space"), "preserve")
    return r2

def replace_in_run(para, run_el, old_sub, new_sub, author, date):
    """
    Find old_sub in run_el and wrap it in w:del / w:ins.
    Returns True if the substitution was made.
    """
    full = run_text(run_el)
    idx = full.find(old_sub)
    if idx == -1:
        return False

    parent = run_el.getparent()
    pos = list(parent).index(run_el)
    parent.remove(run_el)
    ip = pos

    if idx > 0:
        parent.insert(ip, _clone_run(run_el, full[:idx]))
        ip += 1

    # w:del
    d = etree.Element(wt("del"))
    d.set(wt("id"), str(next_id()))
    d.set(wt("author"), author)
    d.set(wt("date"), date)
    rd = copy.deepcopy(run_el)
    for t in rd.findall(wt("t")):
        t.tag  = wt("delText")
        t.text = old_sub
    d.append(rd)
    parent.insert(ip, d); ip += 1

    # w:ins
    ins = etree.Element(wt("ins"))
    ins.set(wt("id"), str(next_id()))
    ins.set(wt("author"), author)
    ins.set(wt("date"), date)
    ri = copy.deepcopy(run_el)
    for t in ri.findall(wt("t")):
        t.text = new_sub
        if " " in new_sub:
            t.set(xs("space"), "preserve")
    ins.append(ri)
    parent.insert(ip, ins); ip += 1

    after = full[idx + len(old_sub):]
    if after:
        parent.insert(ip, _clone_run(run_el, after))

    return True

def replace_all_in_para(para, old_sub, new_sub, author, date):
    """Apply replace_in_run for every occurrence in a paragraph."""
    count = 0
    changed = True
    while changed:
        changed = False
        for run in para.findall(f".//{wt('r')}"):
            if etree.QName(run.getparent().tag).localname == "del":
                continue
            if old_sub in run_text(run):
                if replace_in_run(para, run, old_sub, new_sub, author, date):
                    count += 1
                    changed = True
                    break
    return count

def replace_para_tracked(para, new_text, author, date):
    """
    Replace all direct-run content of a paragraph with a tracked del+ins.
    Used for whole-paragraph reformatting (e.g., reference entries).
    Returns True if a change was made.
    """
    old_runs = para.findall(wt("r"))
    if not old_runs:
        return False
    old_text = "".join(run_text(r) for r in old_runs)
    if not old_text.strip() or old_text.strip() == new_text.strip():
        return False

    tmpl = old_runs[0]
    rpr  = tmpl.find(wt("rPr"))
    ppr  = para.find(wt("pPr"))
    ip   = (list(para).index(ppr) + 1) if ppr is not None else 0

    for r in old_runs:
        para.remove(r)

    # w:del
    d = etree.Element(wt("del"))
    d.set(wt("id"), str(next_id()))
    d.set(wt("author"), author)
    d.set(wt("date"), date)
    rd = etree.SubElement(d, wt("r"))
    if rpr is not None:
        rd.append(copy.deepcopy(rpr))
    dt = etree.SubElement(rd, wt("delText"))
    dt.text = old_text
    dt.set(xs("space"), "preserve")
    para.insert(ip, d)

    # w:ins
    ins = etree.Element(wt("ins"))
    ins.set(wt("id"), str(next_id()))
    ins.set(wt("author"), author)
    ins.set(wt("date"), date)
    ri = etree.SubElement(ins, wt("r"))
    if rpr is not None:
        ri.append(copy.deepcopy(rpr))
    it = etree.SubElement(ri, wt("t"))
    it.text = new_text
    it.set(xs("space"), "preserve")
    para.insert(ip + 1, ins)

    return True

def add_comment(para, anchor_run, comment_text, author, date):
    """
    Anchor a Word comment on anchor_run.
    Returns a dict {id, text, author, date} to be written to comments.xml.
    """
    cid = str(next_id())
    cs  = etree.Element(wt("commentRangeStart")); cs.set(wt("id"), cid)
    ce  = etree.Element(wt("commentRangeEnd"));   ce.set(wt("id"), cid)

    pos = list(para).index(anchor_run)
    para.remove(anchor_run)
    para.insert(pos,     cs)
    para.insert(pos + 1, anchor_run)
    para.insert(pos + 2, ce)

    ref_run = etree.Element(wt("r"))
    rpr2 = etree.SubElement(ref_run, wt("rPr"))
    etree.SubElement(rpr2, wt("rStyle")).set(wt("val"), "CommentReference")
    cr = etree.SubElement(ref_run, wt("commentReference"))
    cr.set(wt("id"), cid)
    para.insert(pos + 3, ref_run)

    return {"id": cid, "author": author, "date": date, "text": comment_text}

def write_comments_xml(comments_path, comment_dicts):
    """Write or append to word/comments.xml."""
    from pathlib import Path
    p = Path(comments_path)
    parser = etree.XMLParser(remove_blank_text=False)
    croot = etree.parse(str(p), parser).getroot() if p.exists() else etree.Element(wt("comments"))

    for cd in comment_dicts:
        cel = etree.SubElement(croot, wt("comment"))
        cel.set(wt("id"),     cd["id"])
        cel.set(wt("author"), cd["author"])
        cel.set(wt("date"),   cd["date"])
        cel.set(wt("initials"), "TAR")
        cp = etree.SubElement(cel, wt("p"))
        cr = etree.SubElement(cp,  wt("r"))
        ct = etree.SubElement(cr,  wt("t"))
        ct.text = cd["text"]
        ct.set(xs("space"), "preserve")

    etree.ElementTree(croot).write(
        str(p), xml_declaration=True, encoding="UTF-8", standalone=True
    )

def ensure_comments_relationship(rels_path, content_types_path):
    """Add comments relationship and content type if not already present."""
    from pathlib import Path
    RELS_NS   = "http://schemas.openxmlformats.org/package/2006/relationships"
    CT_NS     = "http://schemas.openxmlformats.org/package/2006/content-types"
    COMM_TYPE = ("http://schemas.openxmlformats.org/officeDocument"
                 "/2006/relationships/comments")
    parser = etree.XMLParser(remove_blank_text=False)

    rp = Path(rels_path)
    if rp.exists():
        rtree = etree.parse(str(rp), parser)
        rroot = rtree.getroot()
        types = [el.get("Type") for el in rroot.findall(f"{{{RELS_NS}}}Relationship")]
        if COMM_TYPE not in types:
            el = etree.SubElement(rroot, f"{{{RELS_NS}}}Relationship")
            el.set("Id", "rIdComments")
            el.set("Type", COMM_TYPE)
            el.set("Target", "comments.xml")
            rtree.write(str(rp), xml_declaration=True, encoding="UTF-8", standalone=True)

    cp = Path(content_types_path)
    if cp.exists():
        cttree = etree.parse(str(cp), parser)
        ctroot = cttree.getroot()
        parts  = [el.get("PartName") for el in ctroot.findall(f"{{{CT_NS}}}Override")]
        if "/word/comments.xml" not in parts:
            ov = etree.SubElement(ctroot, f"{{{CT_NS}}}Override")
            ov.set("PartName", "/word/comments.xml")
            ov.set("ContentType",
                   "application/vnd.openxmlformats-officedocument"
                   ".wordprocessingml.comments+xml")
            cttree.write(str(cp), xml_declaration=True, encoding="UTF-8", standalone=True)
