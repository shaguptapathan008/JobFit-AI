# 🎯 JobFit AI — AI-Powered Resume and Job Matching

JobFit AI is a Python-based application that analyzes a candidate's resume against a job description. It identifies matching skills, highlights missing skills, calculates a resume-to-job match score, and provides personalized learning recommendations.

The project combines Natural Language Processing (NLP), text similarity, and rule-based skill extraction in an interactive Streamlit web application.

## 🚀 Features

- **Resume Parsing:** Extracts text from uploaded PDF resumes.
- **Job Description Analysis:** Accepts job requirements entered by the user.
- **Resume Matching:** Calculates TF-IDF cosine similarity between resume content and job descriptions.
- **Skill Extraction:** Identifies recognized technical skills using a configurable skills dictionary.
- **Match Score:** Displays an overall matching score, text similarity, and skill coverage.
- **Skill Gap Analysis:** Identifies matching and missing skills.
- **Personalized Recommendations:** Suggests learning activities for missing skills.
- **Interactive Dashboard:** Provides results through a user-friendly Streamlit interface.
- **Automated Testing:** Includes pytest tests for resume parsing and matching functionality.

## 🛠️ Technologies Used

- Python
- Streamlit
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- PyMuPDF
- Scikit-learn
- Regular Expressions
- JSON
- Pytest

## 📂 Project Structure

```text
JobFit-AI/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── matching_engine.py
│   ├── reco.py
│   └── database.py
├── data/
│   └── skills_dictionary.json
├── models/
│   └── README.md
├── tests/
│   ├── test_parser.py
│   ├── test_matching.py
│   └── test_skills.py
└── reports/
    └── .gitkeep
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd JobFit-AI
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 🧪 Running Tests

Run the automated test suite with:

```bash
python -m pytest -v
```

The tests cover core functionality such as PDF text extraction, resume matching, and skill extraction.

## 📊 How It Works

1. The user uploads a PDF resume.
2. PyMuPDF extracts readable text from the document.
3. The user enters a job description.
4. The skill extractor identifies recognized skills in both texts.
5. TF-IDF vectorization and cosine similarity estimate textual similarity.
6. The matching engine calculates skill coverage and an overall score.
7. The application displays matched skills, missing skills, and learning recommendations.

### Matching Score

The current implementation combines text similarity and skill coverage:

**Overall Match Score = (0.60 × Text Similarity) + (0.40 × Skill Coverage)**

Both component scores are expressed as percentages.

This is a heuristic matching score, not a probability of being hired or a guarantee of job suitability.

## 🔮 Future Improvements

- Semantic matching using sentence embeddings.
- Support for additional resume formats.
- Improved skill recognition and synonym handling.
- Resume improvement suggestions.
- Downloadable analysis reports.
- Job recommendation based on candidate profiles.
- Deployment to a public hosting platform.
- More comprehensive automated tests.

## ⚠️ Limitations

- The current PDF parser is intended for text-based PDFs; scanned resumes may require OCR.
- Skill extraction depends on the configured skills dictionary and recognition rules.
- Matching scores are estimates and may not capture all contextual relationships between a candidate's experience and job requirements.
- Recommendations provide general learning guidance rather than a complete personalized training plan.

## 👩‍💻 Project Purpose

JobFit AI demonstrates practical applications of Python, NLP, text similarity, skill extraction, and interactive web development. It is designed as a portfolio project for learning and demonstrating AI/ML engineering skills.

## 📜 License

Choose an appropriate open-source license before distributing this project publicly.
