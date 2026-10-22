
import pytest

from src.matching_engine import (
    calculate_text_similarity,
    match_resume_to_job,
)


def test_text_similarity_for_identical_text():
    text = "Python SQL Pandas machine learning"

    score = calculate_text_similarity(text, text)

    assert score == 100.0


def test_text_similarity_is_between_zero_and_100():
    score = calculate_text_similarity(
        "Python developer with SQL experience",
        "Data analyst using Excel and Power BI",
    )

    assert 0.0 <= score <= 100.0


def test_matching_engine_returns_expected_fields():
    result = match_resume_to_job(
        "Python SQL Pandas machine learning",
        "Python SQL Pandas machine learning Tableau",
    )

    expected_fields = {
        "match_score",
        "text_similarity",
        "skill_coverage",
        "resume_skills",
        "required_skills",
        "matched_skills",
        "missing_skills",
    }

    assert expected_fields.issubset(result.keys())


def test_matching_engine_identifies_missing_skills():
    result = match_resume_to_job(
        "Python and SQL developer",
        "Python SQL and Tableau required",
    )

    assert "python" in result["matched_skills"]
    assert "sql" in result["matched_skills"]
    assert "tableau" in result["missing_skills"]


def test_matching_score_is_within_valid_range():
    result = match_resume_to_job(
        "Python Pandas NumPy",
        "Python SQL Pandas NumPy Scikit-learn",
    )

    assert 0.0 <= result["match_score"] <= 100.0
    assert 0.0 <= result["skill_coverage"] <= 100.0


def test_empty_resume_raises_error():
    with pytest.raises(ValueError):
        match_resume_to_job("", "Python developer required")


def test_empty_job_description_raises_error():
    with pytest.raises(ValueError):
        match_resume_to_job("Python developer", "")


def test_non_string_input_raises_error():
    with pytest.raises(TypeError):
        match_resume_to_job(None, "Python developer")
