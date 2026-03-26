---
name: accounting-lit-search
description: >
  Search and retrieve accounting research papers from top academic journals on behalf of the user.
  Use this skill whenever the user asks to find, search, look up, or review academic literature,
  papers, articles, or prior research in accounting, auditing, or related fields — even if they
  don't use the word "search" explicitly. Triggers include phrases like "what does the literature
  say about", "find me papers on", "what research exists on", "literature review on", or any
  request to surface relevant academic work. Always use this skill when the user is scoping a
  research topic, building a literature review, or asking about evidence from prior studies.
---

# Accounting Literature Search Skill

## Target Journals (search in this priority order)

1. Journal of Accounting Research (JAR) — jar.uchicago.edu
2. Journal of Accounting and Economics (JAE) — sciencedirect.com/journal/journal-of-accounting-and-economics
3. The Accounting Review (TAR) — aaapubs.org/loi/accr
4. Contemporary Accounting Research (CAR) — onlinelibrary.wiley.com/journal/19113846
5. Review of Accounting Studies (RAS) — link.springer.com/journal/11142
6. Accounting, Organizations and Society (AOS) — sciencedirect.com/journal/accounting-organizations-and-society
7. Journal of Accounting and Public Policy (JAPP) — sciencedirect.com/journal/journal-of-accounting-and-public-policy
8. Auditing: A Journal of Practice & Theory (AJPT) — aaapubs.org/loi/ajpt
9. Accounting Horizons (AH) — aaapubs.org/loi/acch

## Workflow

### Step 1: Clarify the query (if needed)
If the user's request is vague, ask one focused clarifying question (e.g., time period, subtopic, methodology preference) before searching. Do not over-ask.

### Step 2: Search
1. **Web search first**: Use `web_search` with targeted queries like:
   - `site:scholar.google.com "[topic]" accounting`
   - `"[topic]" journal of accounting research filetype:pdf`
   - `"[topic]" site:aaapubs.org OR site:jar.uchicago.edu OR site:sciencedirect.com`
   - Vary queries across 3–5 searches to maximize coverage across target journals.
2. **Browser fallback**: If web search returns insufficient results or paywalled abstracts, use Claude in Chrome to:
   - Navigate to Google Scholar: `https://scholar.google.com`
   - Search with query and filter by target journals where possible
   - Navigate to journal websites directly if needed
3. **Login**: If a paper or journal requires authentication, ask the user:
   > "To access full text from [journal], I'll need your login credentials. Would you like to provide them, or should I work from the abstract only?"

### Step 3: Collect and evaluate papers
For each candidate paper, collect:
- Title, authors, year, journal, DOI/URL
- Citation count (from Google Scholar if available)
- Abstract or key excerpts
- Relevance to the user's specific query

### Step 4: Rank papers
Rank by the following criteria **in strict order**:
1. **Relevance** — How directly does it address the user's query? (primary criterion)
2. **Citations** — Higher citation count ranks higher within same relevance tier
3. **Year** — More recent papers rank higher within same relevance + citation tier

Aim for **5–15 papers** depending on query breadth. Cut clearly irrelevant results.

### Step 5: Return results

Format the output as a ranked, numbered list in chat. Use **flexible detail level**:

- **High relevance papers**: Full structured summary
- **Lower relevance papers**: Brief summary (1–2 sentences)

#### Full structured summary format:
```
## [Rank]. [Title] ([Year])
**Authors**: [Author(s)]
**Journal**: [Full journal name]
**Citations**: ~[N] (Google Scholar)
**DOI/Link**: [URL]

**Summary**: [2–4 sentences on research question, method, and findings]

**Relevant to your query**: [1–2 sentences on why this paper is especially relevant]

**Key quote** (APA in-text): "[Quoted sentence or phrase from abstract/paper]" ([Author(s)], [Year], p. [X if available])
```

#### Brief summary format (lower relevance):
```
## [Rank]. [Title] ([Year])
**Authors**: [Author(s)] | **Journal**: [Abbrev.] | **Citations**: ~[N]
[1–2 sentence summary and relevance note.]
```

### Step 6: Offer follow-up
After presenting results, offer:
> "Would you like me to go deeper on any of these, search additional journals, or adjust the ranking criteria?"

## Important notes
- Only cite text that actually appears in accessible content (abstract, open-access full text, or user-authenticated full text). Do not fabricate quotes.
- If citation counts are unavailable, omit that field rather than guessing.
- Always include a DOI or direct URL for each paper.
- If fewer than 3 relevant papers are found, say so and suggest broadening the query.
