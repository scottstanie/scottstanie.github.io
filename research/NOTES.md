# CV maintenance

`cv.yml` is the single source of truth. Everything else in this directory is
generated — **do not hand-edit** `publications-conferences.txt`, `cv-full.md`,
or `cv-industry.md`.

```
make cv        # regenerate all three from cv.yml
make cv-docx   # also emit .docx for uploading to the Google Docs
```

To add a publication: append an entry to `publications:` in `cv.yml` and run
`make cv`. Set `oral: true` for talks (renders the `*`), `selected: true` to
include it in the short industry CV.

## Provenance

`cv.yml` is the merge of two sources that had drifted apart: the plain-text
`publications-conferences.txt` (ahead on conferences) and the Google Docs CV
(ahead on journal articles). 38 entries total, 2018–2026.

Items that were in the text file but missing from the Google Docs CV: Horne
et al. 2022 (*Interpretation*), Fringe 2026, EUSAR 2026, EGU 2026, the OPERA
ATBD, all three AGU 2023 abstracts, both IGARSS 2023 papers, the second Fringe
2023 talk, EGU 2022, and AGU 2018.

Items in the Google Docs CV but missing from the text file: Hänsch et al. 2026
(Data Fusion Contest), the in-prep phase unwrapping paper, the Dataverse data
product, and IGARSS 2021.

## Sections

Publications render into four buckets, set by `SECTIONS` in `render_cv.py`:

| Section | Driven by |
|---|---|
| Journal Articles | `type: journal` |
| Peer-Reviewed Conference Papers | `type: conference` + `peer_reviewed: true` |
| Conference Presentations and Abstracts | `type: conference`, no `peer_reviewed` |
| Data Products and Technical Documents | `type: dataset` / `report` / `thesis` |

The peer-reviewed split exists because you publish into two communities with
opposite conventions: IGARSS and EUSAR proceedings are reviewed, citable papers
indexed in IEEE Xplore, while AGU/EGU/Fringe/LPS abstracts are not peer-reviewed.
Filing them together undersells the IEEE papers to a GRSS reader and makes the
whole list look like padding to a geoscience reader.

Current tally: 10 journal articles (5 first-author), 5 peer-reviewed conference
papers (3 first-author), 20 presentations and abstracts (11 first-author).

DOIs render on the markdown CVs but are suppressed in the plain-text file, which
keeps the UT tracking format as it was.

## Open questions (`needs_check: true` in cv.yml)

- **`igarss2023_ps`** and **`igarss2023_unwrapping`** — no Crossref
  `proceedings-article` record could be found for either, though IEEE does index
  IGARSS 2023. Currently filed as `peer_reviewed: false`. If they did produce
  4-page proceedings papers, flip the flag and add pages/DOI.
- **`lps2025_bekaert`** — first author recorded as "Bekaert, B."; elsewhere he
  appears as "Bekaert, D." Probably a typo, but confirm before publishing.
- **`agu2023_isce3`** — the author list in the source was truncated and does not
  actually include you. Confirm you are a coauthor, or drop the entry.
- **`staniewicz2022_thesis`** — your dissertation, added from `research/pdfs/`.
  It was in neither source. Keep or remove as you prefer.

Resolved since the initial merge:

- **`igarss2020_outlier`** — the two sources disagreed on 2019 vs 2020. Crossref
  gives DOI `10.1109/IGARSS39084.2020.9323893`, pages 6790-6793, confirming 2020.
  Page numbers were absent from both original sources.
- The full CV listed the Graduate Research Assistant role as ending 08/2024,
  conflicting with both the Aug 2022 Ph.D. date and the industry CV. Set to 08/2022.
- The Dolphin JOSS paper is now `selected: true`, so it appears in the industry
  CV. Set it to `false` to restore the old three-item list.

Not yours, but adjacent: IGARSS 2025 has "3D InSAR Time Series for Displacement
Monitoring Utilizing Capella Space Mid-Inclination Orbits" (Bognar et al., incl.
Stringham and Farquharson, DOI 10.1109/IGARSS55030.2025.11243763). You are not
listed as an author.

## Deliberately not automated

Pulling from Google Scholar. Scholar misses Fringe/EUSAR talks and garbles AGU
abstract metadata, which is most of this list — an auto-sync would silently drop
entries. Worth running once a year as a manual cross-check for things you forgot,
not as a build step.
