
"""JobFit AI: resume and job description matching engine."""

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.skill_extractor import extract_skills


def _clean_text(text: str) -> str:
    """Normalize whitespace and letter case."""
    return re.sub(r"\s+", " ", text.lower()).strip()


def calculate_text_similarity(resume_text: str, job_description: str) -> float:
    """Return TF-IDF cosine similarity as a percentage."""
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        sublinear_tf=True,
    )

    try:
        vectors = vectorizer.fit_transform(
            [_clean_text(resume_text), _clean_text(job_description)]
        )
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        return round(float(similarity) * 100, 2)
    except ValueError:
        return 0.0


def match_resume_to_job(
    resume_text: str,
    job_description: str,
) -> dict:
    """Combine text similarity and recognised skill coverage."""
    if not isinstance(resume_text, str) or not isinstance(
        job_description, str
    ):
        raise TypeError("Resume and job description must be strings.")

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    # Uses your existing skill extractor.
    resume_skills = set(extract_skills(resume_text))
    required_skills = set(extract_skills(job_description))

    matched_skills = sorted(resume_skills & required_skills)
    missing_skills = sorted(required_skills - resume_skills)

    skill_coverage = (
        len(matched_skills) / len(required_skills) * 100
        if required_skills
        else 0.0
    )

    text_similarity = calculate_text_similarity(
        resume_text, job_description
    )

    # Initial heuristic weights; evaluate and tune using test examples.
    match_score = 0.60 * text_similarity + 0.40 * skill_coverage

    return {
        "match_score": round(match_score, 2),
        "text_similarity": text_similarity,
        "skill_coverage": round(skill_coverage, 2),
        "resume_skills": sorted(resume_skills),
        "required_skills": sorted(required_skills),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }
