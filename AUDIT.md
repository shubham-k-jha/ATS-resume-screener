# Existing Prototype Audit → Upgrade Record

## What the supplied prototype already did well

- Streamlit UI with PDF/DOCX/TXT upload and paste inputs
- PyMuPDF and python-docx document parsing
- Basic skill taxonomy and synonym matching
- Required/preferred concepts
- TF-IDF with optional Sentence Transformers
- Basic ATS-format checks
- Plotly score visualization
- Automated pytest coverage
- Local in-memory processing intent

## Weaknesses found

1. **Fixed, shallow scoring:** the original engine mixed a small set of components with fixed weights and included certifications/title heuristics that were not tied cleanly to the requested role-specific model.
2. **JD parsing was state-based and fragile:** it could miss required/preferred distinctions in inline requirements.
3. **Resume parsing was section-fragile:** only a few headings were recognized and projects, research, achievements, links, and experience evidence were not structured deeply enough.
4. **Skill taxonomy was too small:** it did not cover many analytics, BI, product, marketing, data-engineering, and data-science terms required by the requested target roles.
5. **Related-skill logic was weak:** it checked parent relationships in a way that could produce misleading matches.
6. **Experience matching was simplistic:** it did not separate direct experience from transferable research experience.
7. **Project analysis was minimal:** it did not assess complexity, methods, results, metrics, or repository evidence.
8. **Communication/presentation/language analysis was absent.**
9. **Evidence transparency was limited:** skill rows did not consistently show the resume evidence supporting a match.
10. **No representative JD library:** only one tiny sample existed.
11. **No role-aware UI:** users could not select a target role or benchmark against multiple role profiles.
12. **No robust export layer:** no JSON/CSV analysis export.
13. **README was too minimal for a serious portfolio project.**
14. **Testing was too narrow:** only two core tests were present.
15. **Error handling and UI were tutorial-level rather than product-level.**

## What was retained

The upgrade keeps the original project's useful foundations: Streamlit, PyMuPDF, python-docx, scikit-learn, Plotly, the local-first processing approach, taxonomy-driven matching, optional semantic embeddings, transparent scoring, and pytest.

## What was replaced or expanded

- Modular source architecture
- Expanded taxonomy and normalization
- Role-aware scoring
- Robust inline and section-style JD parsing
- Structured resume parsing
- Experience/project/achievement/communication/presentation/language analysis
- ATS format diagnostics
- Evidence-level skill matching
- 16 representative original JD profiles
- Recruiter/hiring-manager review surfaces
- JSON/CSV export
- Six automated tests plus library-wide validation
- Professional dashboard layout and styling
- Comprehensive README and deployment documentation
