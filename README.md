<div align="center">

# 🎯 ATS Resume Screener

### **Recruiter-Grade Resume × Job Description Intelligence**

**Understand your match. Find your gaps. Improve your resume.**

<br>

[![Live App](https://img.shields.io/badge/🚀_Live_App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ats--resume-screener.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-ML%2FNLP-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-PDF_Parsing-555555?style=for-the-badge)](https://pymupdf.readthedocs.io/)

<br>

> **A practical ATS and recruiter-style analysis tool for Data Analyst, Data Science, BI, Business Analyst, Product Analyst and related roles.**

</div>

---

## 🚀 Live Demo

<div align="center">

### 👉 **[OPEN ATS RESUME SCREENER](https://ats--resume-screener.streamlit.app/)** 👈

**Upload your resume → choose/paste a JD → analyze → identify gaps → improve.**

</div>

---

## 🧠 What Problem Does It Solve?

Most resume screeners stop at keyword counting.

This project goes further by asking:

```text
┌─────────────────────────────────────────────────────────────┐
│                    RESUME → JOB ANALYSIS                    │
├─────────────────────────────────────────────────────────────┤
│  What is my overall resume health?                         │
│  How closely does my resume fit this specific JD?          │
│  Which required skills are actually evidenced?             │
│  Which important skills are missing?                       │
│  How relevant are my projects?                             │
│  How strong is my experience fit?                           │
│  What would an ATS potentially struggle with?              │
│  What might a recruiter notice first?                      │
│  What should I improve — and why?                          │
└─────────────────────────────────────────────────────────────┘
```

The application is designed to provide **evidence-based guidance**, not a fake guarantee of interviews or selection.

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 📄 Resume Intelligence

- PDF resume upload
- DOCX resume upload
- TXT resume upload
- Paste resume text
- Structured resume parsing
- Contact and section extraction
- Experience analysis
- Project analysis
- Achievement evidence

</td>
<td width="50%">

### 🎯 Job Matching

- Custom JD input
- Built-in representative JD library
- Required vs preferred skills
- Skill normalization and aliases
- Exact skill matching
- Related skill matching
- Missing skill detection
- Semantic similarity
- Role-aware scoring

</td>
</tr>
<tr>
<td>

### 📊 Resume Health

- Overall Resume Health score
- Resume strengths
- Resume weaknesses
- Evidence gaps
- Formatting risks
- Language-quality signals
- Communication signals
- Presentation signals
- Actionable improvement plan

</td>
<td>

### 🧑‍💼 Recruiter Perspective

- Recruiter-style review
- Hiring-manager-style review
- Technical fit
- Role fit
- Project relevance
- Impact evidence
- Potential hesitation points
- Requirement-level resume evidence

</td>
</tr>
</table>

---

# 🔥 Two Different Questions — Two Different Scores

One of the most important design decisions is separating **overall resume quality** from **job-specific compatibility**.

### 🩺 1. Overall Resume Health

Answers:

> **“How strong is my resume independent of one particular job?”**

It examines areas such as:

- structure
- evidence
- achievements
- skills
- project presentation
- readability
- ATS formatting
- professional positioning

### 🎯 2. Job Compatibility

Answers:

> **“How well does this resume match THIS specific job description?”**

It considers:

- required skills
- preferred skills
- semantic JD similarity
- experience
- projects
- tools and technologies
- education
- communication
- presentation
- English/language signals
- ATS formatting

This distinction prevents a resume from being called “bad” simply because it was optimized for a different role.

---

# 📈 Analysis Dashboard

The application is organized into dedicated analysis surfaces:

| Section | What it tells you |
|---|---|
| 🟦 **Overview** | Overall compatibility and major findings |
| 🩺 **CV Health** | Resume quality independent of one JD |
| 🎯 **Role Fit** | How the current resume maps to different target roles |
| 🧩 **Skills** | Required, preferred, related and missing skills |
| 📋 **JD Match** | Requirement-by-requirement alignment |
| 💼 **Experience** | Direct vs transferable experience signals |
| 🚀 **Projects** | Project relevance and evidence |
| 🤖 **ATS Check** | Formatting and ATS-readability risks |
| 🧑‍💼 **Recruiter Review** | First-pass recruiter perspective |
| 🛠️ **Recommendations** | Prioritized actions to improve the resume |
| 🔎 **Resume Evidence** | Evidence supporting important matches |

---

# 🧮 Scoring Methodology

The application uses an **explainable analytical score**, not an employer's private ATS algorithm.

The baseline scoring model combines multiple dimensions:

| Component | Baseline Weight |
|---|---:|
| 🧩 Skill Match | **22%** |
| 🔴 Required Skill Coverage | **18%** |
| 🧠 Semantic JD Match | **12%** |
| 💼 Experience Match | **10%** |
| 🚀 Project Relevance | **8%** |
| 🛠️ Tools / Technology Match | **8%** |
| 🎓 Education Match | **4%** |
| 🏆 Achievement Evidence | **5%** |
| 💬 Communication | **4%** |
| 🎤 Presentation | **2%** |
| ✍️ English / Language Quality | **2%** |
| 🤖 ATS Formatting | **5%** |

> **Important:** These weights are an analytical model created for this application. They are **not** the weighting system of LinkedIn, Indeed, Workday, Greenhouse, Lever, or any employer ATS.

Role-aware adjustments are used so that Data Analyst and Data Scientist profiles are not treated as identical.

---

# 🧩 Skill Matching

The application does more than search for identical strings.

### Example

```text
Job Description
────────────────────────────────────
Advanced SQL
PostgreSQL
Power BI
Data Visualization

Resume
────────────────────────────────────
SQL
MySQL
Power BI
Plotly
Dashboard Development
```

The analysis can distinguish between:

- ✅ Direct matches
- 🔗 Related/normalized matches
- ⚠️ Partial evidence
- ❌ Missing requirements

Skill aliases and taxonomy normalization help map variations such as:

```text
PowerBI     → Power BI
Postgres    → PostgreSQL
ML          → Machine Learning
```

The taxonomy is extensible through the project's skill data files.

---

# 🧠 Semantic Matching

Where available, the application can use **Sentence Transformers** for semantic similarity.

If the optional semantic model cannot be loaded, the application falls back to **TF-IDF cosine similarity** so that the core workflow remains usable without an external LLM API.

```text
Resume Text ─────────────┐
                         ├──► Semantic Similarity ──► JD Fit
Job Description ─────────┘
```

Semantic similarity is treated as **one signal among several**, not as a replacement for evidence-based skill and experience matching.

---

# 📝 Missing Skills & Gaps

The screener is designed to answer the question candidates actually care about:

> **“Why isn't my resume matching this job strongly enough?”**

It surfaces areas such as:

```text
🔴 Critical / Required Gaps
🟠 Important Gaps
🟡 Preferred Gaps
🟢 Strong Matches
```

Recommendations should be based on genuine evidence.

The system should **never recommend inventing a skill, project, achievement, metric, certification or experience that the candidate does not have.**

---

# 🩺 Resume Health Analysis

The application also evaluates the resume **without requiring a specific JD**.

Typical areas include:

- Resume structure
- Section quality
- Skills positioning
- Experience evidence
- Project evidence
- Achievement strength
- Communication signals
- Professional writing
- ATS formatting risks
- Overall role positioning

This makes the tool useful for improving a master resume before applying to individual jobs.

---

# 🎯 Role Likeness

The application can compare the current resume against multiple target role profiles.

Example categories:

```text
Data Analyst
Data Scientist
Business Analyst
BI Analyst
Product Analyst
Marketing Analyst
Financial Data Analyst
Operations Analyst
Reporting Analyst
Junior Data Scientist
Associate Data Scientist
Machine Learning Analyst
Analytics Engineer
Custom Role
```

The result is a **role-likeness signal based on the evidence currently present in the resume**, not a claim about employability or hiring probability.

---

# 📚 Representative Job Description Library

The project includes original representative job profiles covering areas such as:

- Data Analyst — Entry Level
- Data Analyst — SQL / BI
- Data Analyst — Mid Level
- Operations Analyst
- Financial Data Analyst
- Data Scientist — Entry Level
- Machine Learning / Data Science
- NLP / Applied Data Science
- Forecasting / Time Series
- Business Analyst
- BI Analyst
- Reporting Analyst
- Product Analyst
- Marketing Analyst
- Analytics Engineer

These are **representative sample JDs**, not scraped live job postings.

The project intentionally avoids reproducing copyrighted job descriptions from job boards or company career pages.

---

# 🧑‍💼 Recruiter Review

The recruiter-review layer focuses on questions a first-pass reviewer may ask:

- What stands out?
- Is the target role obvious?
- Are the required skills actually evidenced?
- Is there meaningful project evidence?
- Are achievements measurable where appropriate?
- What may cause hesitation?
- What looks unclear or weak?
- Is the candidate's background relevant to the role?

It is an **analytical simulation**, not a prediction of what a specific recruiter will decide.

---

# 🛠️ Actionable Recommendations

The goal is not simply to say:

> “Your resume needs improvement.”

The application is designed to move from diagnosis to action:

```text
CURRENT
   ↓
What is weak or missing?
   ↓
EVIDENCE
   ↓
What does the resume currently prove?
   ↓
RECOMMENDATION
   ↓
What should be improved?
   ↓
WHY
   ↓
Why does this matter for the target role?
```

Recommendations remain evidence-based and should not fabricate candidate claims.

---

# 📊 Interactive Visualizations

The dashboard uses Plotly where visual analysis adds value.

Examples include:

- 📊 Score breakdown
- 🧩 Skill match visualization
- 🎯 Role-likeness comparison
- 📈 Category-level scores
- 🔴 Required vs preferred skill analysis

The goal is to make the analysis **auditable and understandable**, rather than adding charts purely for decoration.

---

# 🏗️ Project Architecture

```text
ats-resume-screener/
│
├── app.py                         # Streamlit application
│
├── src/
│   ├── ats_checker.py             # ATS formatting checks
│   ├── config.py                  # Configuration
│   ├── document_parser.py         # Document extraction
│   ├── exporter.py                # JSON / CSV exports
│   ├── jd_library.py              # Sample JD library
│   ├── jd_parser.py               # JD parsing
│   ├── recommendations.py         # Improvement recommendations
│   ├── resume_health.py           # Resume health analysis
│   ├── resume_parser.py           # Resume structure/evidence
│   ├── scoring.py                 # Role-aware scoring
│   ├── semantic_matcher.py        # Semantic similarity
│   └── taxonomy.py                # Skill normalization
│
├── data/
│   ├── job_descriptions/
│   │   ├── library.json
│   │   └── README.md
│   │
│   └── skills/
│       └── skill_taxonomy.json
│
├── tests/
│   └── test_core.py
│
├── assets/
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧰 Technology Stack

<div align="center">

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core application and analysis |
| 🎈 **Streamlit** | Interactive web application |
| 🐼 **Pandas** | Data processing |
| 🔢 **NumPy / Python** | Numerical processing where required |
| 🤖 **scikit-learn** | TF-IDF, similarity and analytical scoring |
| 🧠 **Sentence Transformers** | Optional semantic matching |
| 📄 **PyMuPDF** | PDF text extraction |
| 📝 **python-docx** | DOCX parsing |
| 📊 **Plotly** | Interactive visualizations |
| 🧪 **Pytest** | Automated testing |

</div>

---

# ⚡ Quick Start

### 1️⃣ Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd ats-resume-screener
```

### 2️⃣ Create a virtual environment

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

### 5️⃣ Open the local Streamlit URL

Streamlit will display the local address in your terminal.

---

# 🔬 Typical Workflow

```text
1. Upload / paste resume
          ↓
2. Select target role
          ↓
3. Choose sample JD OR paste custom JD
          ↓
4. Analyze resume
          ↓
5. Review Resume Health
          ↓
6. Review Job Compatibility
          ↓
7. Inspect matched + missing skills
          ↓
8. Review experience + project fit
          ↓
9. Check ATS formatting risks
          ↓
10. Read recruiter-style review
          ↓
11. Follow prioritized recommendations
          ↓
12. Export analysis if required
```

---

# 📤 Export

The application provides analysis exports such as:

- **JSON analysis report**
- **CSV score breakdown**

These can be used for tracking changes between resume versions or reviewing results outside the Streamlit interface.

---

# 🧪 Testing

Run the automated test suite with:

```bash
pytest -q
```

The test coverage includes core behaviors such as:

- Skill aliases
- Resume section/contact extraction
- Required vs preferred classification
- Score bounds
- Missing required skills
- ATS formatting risk detection

The project is structured so additional tests can be added for parser edge cases, specialized roles and larger benchmark datasets.

---

# ☁️ Streamlit Deployment

### Deploy your own copy

1. Push the project to GitHub.
2. Open **Streamlit Community Cloud**.
3. Connect your GitHub repository.
4. Select `app.py` as the main application file.
5. Deploy.
6. Copy the generated Streamlit URL.
7. Update the Live Demo link in this README if you are publishing your own deployment.

### Current live application

👉 **[https://ats--resume-screener.streamlit.app/](https://ats--resume-screener.streamlit.app/)**

---

# 🔐 Privacy & Data Handling

Resume files can contain sensitive personal information.

The project follows a local-first processing philosophy:

- Resume analysis is performed inside the application workflow.
- No external LLM is required for the core analysis.
- Resume content should not be unnecessarily logged.
- External services should not receive resume content unless explicitly configured.
- Users should review hosting and privacy requirements before uploading confidential resumes to a public deployment.

> **Do not upload confidential candidate information to a public demo unless you are comfortable with the deployment environment and its data-handling policies.**

---

# ⚠️ Important Limitations

### ATS scores are estimates

There is no universal ATS score. Different employers use different systems, configurations, parsing rules and screening workflows.

Therefore:

> **This application's ATS score is an analytical estimate for resume improvement — not an official employer ATS score.**

### Other limitations

- PDF extraction depends on document structure.
- Scanned PDFs may require OCR that is outside the core workflow.
- Multi-column PDFs can produce imperfect reading order.
- Skill taxonomy coverage is finite.
- Semantic similarity does not prove actual competence.
- Experience extraction is heuristic for complex career histories.
- Sample JDs are not live job postings.
- The tool does not guarantee interviews, callbacks or offers.

---

# 🗺️ Roadmap

```text
✅ Resume parsing
✅ JD parsing
✅ Skill taxonomy
✅ Required / preferred matching
✅ Semantic similarity
✅ Role-aware scoring
✅ Resume Health analysis
✅ ATS formatting analysis
✅ Recruiter-style review
✅ Actionable recommendations
✅ Representative JD library
✅ JSON / CSV export

🔜 OCR for scanned resumes
🔜 Larger benchmark dataset
🔜 Batch resume-to-JD comparison
🔜 Resume version comparison
🔜 More advanced evidence extraction
🔜 Custom scoring-weight editor
🔜 Multilingual resume analysis
🔜 Expanded recruiter/hiring-manager analytics
```

---

# 💼 Portfolio Value

This project demonstrates practical experience across:

```text
Python
│
├── Document Processing
├── NLP / Information Extraction
├── Semantic Similarity
├── Machine Learning Concepts
├── Rule-Based Intelligence
├── Data Analysis
├── Scoring Systems
├── Explainable Recommendations
├── Interactive Dashboards
├── Streamlit Development
├── Data Visualization
├── Software Architecture
└── Automated Testing
```

It is intentionally positioned as a **real analytical application**, rather than a simple keyword counter or beginner Streamlit demo.

---

# 🧭 Design Principles

| Principle | Meaning |
|---|---|
| 🎯 **Evidence > Claims** | Match what the resume actually demonstrates |
| 🧠 **Explainability > Black Box** | Scores should have understandable components |
| 🧩 **Fit > Keywords** | Context matters more than raw keyword counts |
| 📌 **JD-specific > Generic** | A resume can fit one role better than another |
| 🔍 **Gaps > Guessing** | Missing evidence should be visible |
| 🔐 **Privacy > Convenience** | Resume data deserves careful handling |
| 🚫 **Truth > Keyword Stuffing** | Never invent qualifications |

---

# ❌ What This Project Does NOT Claim

This application does **not** claim to:

- reproduce a private employer ATS
- predict hiring decisions
- guarantee interviews
- guarantee selection
- know an employer's exact screening weights
- prove that a candidate possesses a skill merely because a keyword appears
- replace a human recruiter or hiring manager

It is a decision-support and resume-improvement tool.

---

# 📸 Screenshots

Add real screenshots here after capturing them from the deployed application:

```text
assets/
├── dashboard.png
├── resume-health.png
├── skills.png
├── jd-match.png
├── ats-check.png
└── recruiter-review.png
```

Example Markdown once the images exist:

```markdown
![ATS Dashboard](assets/dashboard.png)
![Resume Health](assets/resume-health.png)
![Skill Analysis](assets/skills.png)
```

> **Do not add placeholder screenshots as if they were real application captures.**

---

# 🤝 Contributing

Contributions are welcome for:

- New skill aliases
- Better parsing rules
- Additional representative JDs
- Improved scoring calibration
- More tests
- Better accessibility
- UI improvements
- Additional evidence extraction

When adding functionality, preserve the project's evidence-first approach and avoid fabricated candidate or job information.

---

# 👨‍💻 Author

## **Shubham Jha**

**Data Analytics / Data Science | Python | SQL | Power BI | Machine Learning | Streamlit**

This project is part of a portfolio focused on building practical analytics and data-science applications.

### 🔗 Connect

- 💼 **LinkedIn:** [Shubham Jha](https://linkedin.com/in/shubhamkjha-datascience)
- 🐙 **GitHub:** [shubhamkjha-datascience](https://github.com/shubhamkjha-datascience)
- 🚀 **Live ATS Screener:** [Open App](https://ats--resume-screener.streamlit.app/)

---

<div align="center">

## ⭐ If this project is useful, consider starring the repository!

### **Resume → Evidence → Match → Gaps → Action**

**Built to help candidates understand their resume — not to manufacture one.**

</div>
