# Majumder Lab website and CV review

Reviewed 4 November 2026. Local source is prepared for a hosting test upload. No deployment was performed.

## Changes made

- Proofread all seven HTML pages, including expanded research descriptions and older news entries.
- Standardized degree names, institutional names, spelling, and authorship notation.
- Corrected the final published titles of the Cat1, Cad1, and Cam1 articles. Restored Marianna Teplova to the Cad1 author list and corrected Swati Dubey's surname in the LysO citation.
- Corrected Cap1 to co-first author in the CV overview and research narrative, matching the preprint's equal-contribution statement.
- Regenerated the five-page CV, retained its bookmarks and clickable links, and synchronized the downloadable website copy.
- Added page descriptions, a favicon, correct active navigation on Home, image dimensions, and clearer PDF link labels.
- Repaired the outdated DST fellowship link and replaced the unavailable camel research centre link with ICAR's official institute directory.
- Compressed news and team images, including the Cat1 animation, reducing referenced downloads by approximately 18 MB. Original images remain in the checkout.
- Preserved the first research figure's natural proportions with automatic CSS height scaling. The original is 943 × 913 pixels. Added automatic image height scaling to the shared base styles to prevent similar distortion elsewhere.
- Retained the requested portrait-only G. N. Ramachandran lecture image.

- Reduced the Team portrait to 100 × 110 CSS pixels on phones, using contain to retain the full photo. Capped the legacy Profile portrait on phones as well.

## Verification

- All seven HTML pages pass local structural checks, with one main heading each and no duplicate IDs or unbalanced elements.
- All 23 image instances decode successfully and have alternative text and intrinsic dimensions.
- All local page, stylesheet, image, PDF, and fragment destinations resolve.
- Checked public metadata for all eight published journal articles through Crossref, and both preprints through bioRxiv.
- Checked all 36 distinct external URLs. Repaired the two unavailable destinations; their replacements return HTTP 200. Four other destinations returned access restrictions (Science, RSC, Cell Host & Microbe, and ResearchGate); these are not evidence of broken links.
- Inspected rendered PNGs of all five CV pages. Checked PDF text bounds, five bookmarks, 28 link annotations, and matching download copies.
- Reviewed representative desktop layouts and 375-pixel browser previews. The final research image height correction was checked in source and in the packaged stylesheet; the browser automation subsequently timed out, so it has not received a fresh visual check.
- Verified the ZIP's integrity, required file inclusion, and exact CV bytes. The package contains no Git metadata, temporary review scripts, previous CVs, or working files.

## Handoff

Unzip `Majumder_Lab_Ready_to_Upload.zip` into the hosting web root, preserving paths. It is a static site and needs no build or database. Open Home, Team, Research, Publications, Work with us, and News on the hosting test URL, and test the CV link before announcing the final URL. Refresh cached styles to see the research image correction.

The final host's HTTPS, response headers, and deployment configuration remain outside this local review. The personal career dates, invitation details, memberships, and Cap1 journal acceptance were retained from the supplied content; public bibliographic metadata does not independently establish all of those facts.

The EMSI 2026 organizer currently states its conference website will retire on 15 November 2026. Revisit those historical source links if the organizer removes the site.

## Reference records

- [Crossref REST API](https://api.crossref.org/works/10.1016/j.cell.2024.10.002)
- [Cap1 preprint](https://www.biorxiv.org/content/10.1101/2025.11.13.688252v1)
- [Chp1 preprint](https://www.biorxiv.org/content/10.64898/2026.08.05.743128v1)
- [IIT Kharagpur faculty profile](https://www.iitkgp.ac.in/department/BT/faculty/bt-puja)
- [DST WISE-KIRAN](https://dst.gov.in/scientific-programmes/wise-kiran)
- [ICAR institute directory](https://icar.gov.in/en/animal-science/institutes-universities-under-animal-science-division)
- [EMSI 2026](https://emsi2026.iitkgp.ac.in/)
