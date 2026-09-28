# ATS Resume Screener

> **Recruiter-grade Resume × Job Description Intelligence**

A local-first Streamlit application that analyzes a resume against a specific job description for Data Analyst, Data Science, Business Intelligence, Business Analyst, Product Analyst, Marketing Analyst, and related roles.

## 🚀 Live Streamlit App

🔗 **Streamlit App:** [[ADD STREAMLIT DEPLOYED APP LINK HERE](https://ats--resume-screener.streamlit.app/)]

> Replace the placeholder only after deploying your own repository. No live URL is invented by this project.

## Why this project

Keyword counting alone does not explain resume-to-JD fit. This project combines document parsing, skill normalization, required/preferred classification, semantic similarity, experience and project evidence, ATS formatting checks, communication/presentation signals, recruiter-style review, and transparent recommendations.

## Key Features

- PDF, DOCX and TXT resume/JD ingestion
- Paste-text input for both resume and JD
- 16 original representative sample JDs
- Role-aware scoring for analyst and data-science profiles
- Skill taxonomy with aliases such as `PowerBI → Power BI`, `Postgres → PostgreSQL`, `ML → Machine Learning`
- Required vs preferred skill analysis
- Exact, related, and missing skill classification
- Optional Sentence Transformer semantic similarity with TF-IDF fallback
- Transferable research experience surfaced separately from direct industry experience
- Project relevance and measurable-evidence analysis
- Communication, presentation and professional-writing signals
- ATS formatting risk checks
- Recruiter and hiring-manager style review
- Requirement-level resume evidence
- JSON and CSV export
- Automated tests
- Local-first processing; no external LLM is required

## Supported Roles

Data Analyst, Data Scientist, Business Analyst, BI Analyst, Product Analyst, Marketing Analyst, Financial Data Analyst, Operations Analyst, Reporting Analyst, Junior Data Scientist, Associate Data Scientist, Machine Learning Analyst, Analytics Engineer, and Custom Role.

## Estimated ATS Match Score

The application displays an **Estimated ATS Match Score**, not an official employer ATS score.

The baseline model uses these explainable components:

| Component | Baseline weight |
|---|---:|
| Skill Match | 22% |
| Required Skill Coverage | 18% |
| Semantic JD Match | 12% |
| Experience Match | 10% |
| Project Relevance | 8% |
| Tools/Technology Match | 8% |
| Education Match | 4% |
| Achievement Evidence | 5% |
| Communication | 4% |
| Presentation | 2% |
| English/Language Quality | 2% |
| ATS Formatting | 5% |

Weights are normalized to 100 and adjusted by role family. For example, Data Scientist profiles place more emphasis on required skills, machine-learning projects, semantic fit, and technical evidence, while analyst profiles emphasize SQL/BI/business-analysis fit and communication.

Every displayed component has a visible score and the skill tab exposes exact/related/missing evidence. The score is an analytical estimate intended for resume improvement, not a hiring prediction.

## Job Description Library

The built-in library contains original representative profiles covering:

- Data Analyst: entry, SQL + Power BI, mid-level, operations, financial
- Data Scientist: entry, machine learning, NLP, forecasting, applied data science
- Business Analyst
- BI Analyst
- Reporting Analyst
- Product Analyst
- Marketing Analyst
- Analytics Engineer

The library is explicitly labeled as **Representative sample**. It is not a feed of live jobs and does not reproduce job-board text.

## NLP / Semantic Matching

The semantic layer uses Sentence Transformers when the model is available locally. If that optional model cannot load, the application falls back to TF-IDF cosine similarity. This keeps the core application functional without requiring an external API.

## Recruiter Review

The review surface asks evidence-based questions:

- What stands out?
- What may cause hesitation?
- Are required skills evidenced?
- Is the target role clear?
- Is there enough project and impact evidence?

It does not claim to predict a particular employer's hiring decision.

## Project Architecture

```text
ats-resume-screener/
├── app.py
├── src/
│   ├── ats_checker.py
│   ├── config.py
│   ├── document_parser.py
│   ├── exporter.py
│   ├── jd_library.py
│   ├── jd_parser.py
│   ├── recommendations.py
│   ├── resume_parser.py
│   ├── scoring.py
│   ├── semantic_matcher.py
│   └── taxonomy.py
├── data/
│   ├── job_descriptions/
│   │   ├── README.md
│   │   └── library.json
│   └── skills/
│       └── skill_taxonomy.json
├── tests/
│   └── test_core.py
├── assets/
├── .streamlit/config.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Local Setup

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit, upload a resume, select a target role, select or paste a JD, and click **Analyze Resume**.

## Testing

```bash
pytest -q
```

Tests cover skill aliases, resume sections/contact extraction, required/preferred classification, score bounds, missing required skills, and ATS-format risk detection.

## Streamlit Deployment

1. Push this project to a GitHub repository.
2. Open Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select `app.py` as the main file.
5. Deploy.
6. Copy the deployed URL.
7. Replace `[ADD STREAMLIT DEPLOYED APP LINK HERE]` in this README with the actual URL.

The app does not invent or reserve a deployed URL.

## 📸 Screenshots

Optional placeholders — only add these after creating the actual images:

```text
### Dashboard
![ATS Dashboard](assets/dashboard.png)

### Skill Analysis
![Skill Analysis](assets/skills.png)

### Recruiter Review
![Recruiter Review](assets/recruiter-review.png)
```

## Privacy

Resume text is processed within the Streamlit application session. The application does not intentionally send resume content to an external LLM or ATS service. If you deploy publicly, review Streamlit hosting, logs, file-upload behavior, and your organization's privacy requirements before using real candidate data.

## Limitations

- ATS implementations differ across employers and vendors; this score cannot reproduce an employer's private ranking model.
- PDF layout analysis is limited to extracted text and basic metadata. Scanned PDFs are detected but OCR is not included.
- Multi-column reading order can vary by source PDF.
- Skill taxonomy coverage is finite and should be expanded for specialized roles.
- Semantic matching is not a guarantee of conceptual equivalence.
- Years-of-experience extraction is heuristic and should be reviewed for complex career histories.
- The application does not browse live job postings.

## Future Improvements

- Optional consent-based OCR
- More robust multi-column PDF layout analysis
- spaCy-based entity/date extraction
- Human-reviewed calibration dataset
- Batch resume-to-JD comparison
- Custom role-weight editor
- Multilingual resume analysis
- Authenticated multi-user deployment
- Optional organization-controlled LLM layer with explicit consent and data controls

## Portfolio Positioning

This project demonstrates:

`Python` · `Streamlit` · `NLP` · `Information Extraction` · `Semantic Search` · `scikit-learn` · `Data Analysis` · `Plotly` · `Software Engineering` · `Recruiter/ATS Analytics`

## Author

**Shubham Jha** — Data Analytics / Data Science portfolio project.

Connect with me through the links you choose to publish in your GitHub profile or resume.
