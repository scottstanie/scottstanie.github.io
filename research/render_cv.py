#!/usr/bin/env python3
"""Render every CV variant from research/cv.yml.

Outputs:
    publications-conferences.txt   UT-format list (the one your advisor asked for)
    cv-full.md                     full academic CV
    cv-industry.md                 short industry CV (selected publications only)

Run `python3 research/render_cv.py`, or `make cv` from the repo root.
"""

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
CV_YML = HERE / "cv.yml"

def _is(*types, peer_reviewed=None):
    def pred(p):
        if p["type"] not in types:
            return False
        return peer_reviewed is None or bool(p.get("peer_reviewed")) is peer_reviewed
    return pred


# (heading, predicate). Order here is the order on the rendered CV.
SECTIONS = [
    ("Journal Articles", _is("journal")),
    ("Peer-Reviewed Conference Papers", _is("conference", peer_reviewed=True)),
    ("Conference Presentations and Abstracts", _is("conference", peer_reviewed=False)),
    ("Data Products and Technical Documents", _is("dataset", "report", "thesis")),
]


def format_authors(authors):
    """APA-ish join. A literal '...' element renders as an elision."""
    assert authors, "entry has no authors"
    if len(authors) == 1:
        return authors[0]
    head, last = authors[:-1], authors[-1]
    joined = ", ".join(head)
    if last == "...":          # list trails off: "A, B, ..."
        return f"{joined}, ..."
    if head[-1] == "...":      # elision before final author: "A, ... & C"
        return f"{joined} & {last}"
    return f"{joined}, & {last}"


def format_citation(pub, bold_self=None, include_doi=True):
    """One reference string. `bold_self` wraps matching authors in ** for markdown."""
    authors = pub["authors"]
    if bold_self:
        authors = [f"**{a}**" if bold_self in a else a for a in authors]

    parts = [f"{format_authors(authors)} ({pub['year']}). {pub['title'].rstrip('.')}."]

    venue = pub.get("venue")
    if venue:
        tail = venue
        if pub.get("volume"):
            vol = pub["volume"]
            tail += f", {vol}({pub['issue']})" if pub.get("issue") else f", {vol}"
            if pub.get("pages"):
                tail += f", {pub['pages']}"
        elif pub.get("pages"):
            tail += f" (pp. {pub['pages']})"
        if pub.get("abstract_id"):
            tail += f", Abstract {pub['abstract_id']}"
        parts.append(tail if tail.endswith(".") else tail + ".")

    if pub.get("location"):
        loc = pub["location"]
        parts.append(loc if loc.endswith(".") else loc + ".")
    if pub.get("doi") and include_doi:
        parts.append(f"https://doi.org/{pub['doi']}")
    if pub.get("status") == "in-prep":
        parts.append("In prep.")

    return " ".join(parts)


def is_first_author(pub, self_regex):
    return self_regex in pub["authors"][0]


def publication_summary(cv):
    """One-line tally: the first thing a reader's eye lands on."""
    pubs, me = cv["publications"], cv["personal"]["self_regex"]
    bits = []
    for title, pred in SECTIONS[:3]:
        entries = [p for p in pubs if pred(p)]
        if not entries:
            continue
        first = sum(1 for p in entries if is_first_author(p, me))
        label = title.replace("Peer-Reviewed ", "").replace("Articles", "articles").lower()
        bits.append(f"{len(entries)} {label} ({first} first-author)")
    return "*" + "; ".join(bits) + ".*"


def render_txt(cv):
    """The plain-text tracking format, regenerated verbatim from cv.yml."""
    pubs = cv["publications"]
    out = []
    for title, pred in SECTIONS:
        entries = [p for p in pubs if pred(p)]
        if not entries:
            continue
        rule = "-" * len(title)
        out.append(f"{rule}\n{title}\n{rule}\n" if out else f"{title}\n{rule}\n")
        for p in entries:
            star = "*" if p.get("oral") else ""
            out.append(star + format_citation(p, include_doi=False) + "\n")
    out.append("* indicates oral presentation")
    return "\n".join(out) + "\n"


def render_md(cv, industry=False):
    """Markdown CV. `industry` gives the short variant."""
    me = cv["personal"]
    L = [f"# {me['name']}", ""]
    L.append(f"{me['site']} | {me['email']} | Github: {me['github']}")
    L.append("")

    def heading(text):
        L.extend([f"## {text}", ""])

    if industry:
        heading("Experience")
        for job in cv["experience"]:
            if job["title"].startswith("Summer Internship"):
                continue
            L.append(f"**{job['title']}** | {job['org']}, {job['location']} | {job['start']} – {job['end']}")
            L.append("")
            L.extend(f"- {b}" for b in job["bullets"])
            L.append("")
        heading("Education")
        for e in cv["education"]:
            L.append(f"- {e['degree']}, {e['institution']} ({e['end']}){', ' + e['note'] if e.get('note') else ''}")
        L.append("")
    else:
        heading("Education")
        for e in cv["education"]:
            L.append(f"**{e['institution']}**, {e['location']}")
            L.append("")
            L.append(f"{e['degree']}{', ' + e['note'] if e.get('note') else ''} ({e['end']})")
            L.append("")
        heading("Research and Work Experience")
        for job in cv["experience"]:
            L.append(f"**{job['org']}**, {job['location']}")
            L.append("")
            L.append(f"*{job['title']}* ({job['start']} – {job['end']})")
            L.append("")
            L.extend(f"- {b}" for b in job["bullets"])
            L.append("")

    heading("Technical Skills")
    for k, v in cv["skills"].items():
        L.extend([f"**{k}**", "", v, ""])

    if not industry:
        heading("Teaching Experience")
        for t in cv["teaching"]:
            L.append(f"**{t['org']}**, {t['location']}")
            L.append("")
            L.append(f"{t['course']} ({t['when']})")
            L.append("")

    heading("Honors and Awards")
    awards = [a for a in cv["awards"] if a.get("selected")] if industry else cv["awards"]
    L.extend(f"- {a['name']}, {a['year']}" for a in awards)
    L.append("")

    pubs = cv["publications"]
    me = cv["personal"]["self_regex"]
    if industry:
        heading("Selected Publications")
        L.extend(f"- {format_citation(p, bold_self=me)}" for p in pubs if p.get("selected"))
        L.append("")
    else:
        heading("Publications and Presentations")
        L.extend([publication_summary(cv), ""])
        for title, pred in SECTIONS:
            entries = [p for p in pubs if pred(p)]
            if not entries:
                continue
            L.extend([f"### {title}", ""])
            L.extend(f"- {format_citation(p, bold_self=me)}" for p in entries)
            L.append("")

    if not industry:
        heading("Leadership and Service")
        L.extend(f"- {s}" for s in cv["service"])
        L.append("")
        heading("Professional Affiliations")
        L.append(", ".join(cv["affiliations"]))
        L.append("")

    return "\n".join(L)


def main():
    cv = yaml.safe_load(CV_YML.read_text())
    pubs = cv["publications"]

    keys = [p["key"] for p in pubs]
    assert len(keys) == len(set(keys)), f"duplicate keys: {[k for k in keys if keys.count(k) > 1]}"
    for p in pubs:
        assert sum(pred(p) for _, pred in SECTIONS) == 1, f"{p['key']} matches no/multiple sections"
    assert any(p.get("selected") for p in pubs), "industry CV would have no publications"

    pubs.sort(key=lambda p: (-int(p["year"]), p["key"]))

    targets = {
        "publications-conferences.txt": render_txt(cv),
        "cv-full.md": render_md(cv, industry=False),
        "cv-industry.md": render_md(cv, industry=True),
    }
    for name, text in targets.items():
        (HERE / name).write_text(text)
        print(f"wrote {name} ({len(text.splitlines())} lines)")

    flagged = [p["key"] for p in pubs if p.get("needs_check")]
    if flagged:
        print(f"\n{len(flagged)} entries flagged needs_check: {', '.join(flagged)}", file=sys.stderr)


if __name__ == "__main__":
    main()
