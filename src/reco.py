
"""JobFit AI: personalised skill-gap recommendations."""

from typing import Any


SKILL_GUIDANCE = {
    "python": (
        "Practise Python fundamentals, functions, data structures, "
        "file handling, and small automation projects."
    ),
    "sql": (
        "Practise SELECT, filtering, JOINs, GROUP BY, subqueries, "
        "and window functions using a sample database."
    ),
    "machine learning": (
        "Study supervised and unsupervised learning, model evaluation, "
        "overfitting, and cross-validation with scikit-learn."
    ),
    "pandas": (
        "Practise data cleaning, filtering, groupby, merge, and "
        "missing-value handling with real datasets."
    ),
    "numpy": (
        "Practise arrays, indexing, vectorisation, and numerical "
        "operations on datasets."
    ),
    "scikit-learn": (
        "Build a complete ML workflow with preprocessing, train/test "
        "splits, pipelines, and evaluation metrics."
    ),
    "deep learning": (
        "Learn neural-network fundamentals, activation functions, "
        "loss functions, and backpropagation."
    ),
    "natural language processing": (
        "Practise text cleaning, tokenisation, TF-IDF, and text "
        "classification on a public dataset."
    ),
    "excel": (
        "Practise lookup functions, PivotTables, charts, and "
        "Power Query on a business dataset."
    ),
    "power bi": (
        "Build an interactive dashboard and practise data modelling, "
        "DAX measures, and report design."
    ),
    "tableau": (
        "Create interactive charts and dashboards with filters "
        "and calculated fields."
    ),
    "data analysis": (
        "Complete an exploratory data analysis project and explain "
        "the business insights you discover."
    ),
    "data visualization": (
        "Practise selecting suitable charts and communicating "
        "patterns with Matplotlib, Seaborn, or a BI tool."
    ),
    "statistics": (
        "Review descriptive statistics, probability, distributions, "
        "hypothesis testing, and confidence intervals."
    ),
    "computer vision": (
        "Practise image preprocessing, image classification, "
        "and evaluation using a public image dataset."
    ),
    "git": (
        "Practise commits, branches, merges, and publishing a "
        "well-documented project on GitHub."
    ),
    "streamlit": (
        "Build a small interactive Python application with inputs, "
        "charts, and a clear results page."
    ),
    "docker": (
        "Learn Dockerfiles, images, containers, and how to package "
        "a Python application reproducibly."
    ),
    "aws": (
        "Learn the basics of cloud storage, compute, permissions, "
        "and deploying a small application."
    ),
    "generative ai": (
        "Explore language models, prompt design, embeddings, "
        "and evaluation of generated outputs."
    ),
    "large language models": (
        "Learn tokenisation, embeddings, retrieval-augmented "
        "generation, and how to evaluate LLM outputs."
    ),
}


def generate_recommendations(result: dict[str, Any]) -> list[str]:
    """Generate learning suggestions from a matching-engine result.

    Expected input: the dictionary returned by match_resume_to_job().
    Recommendations are learning suggestions, not hiring predictions.
    """
    if not isinstance(result, dict):
        raise TypeError("Result must be a dictionary.")

    missing_skills = result.get("missing_skills", [])

    if not isinstance(missing_skills, (list, tuple, set)):
        raise TypeError("missing_skills must be a list, tuple, or set.")

    recommendations = []

    for skill in sorted(set(missing_skills)):
        if not isinstance(skill, str):
            continue

        normalized_skill = skill.strip().lower()
        if not normalized_skill:
            continue

        guidance = SKILL_GUIDANCE.get(
            normalized_skill,
            (
                f"Study {skill}, practise it with a small hands-on "
                "exercise, and document what you learn in a project."
            ),
        )

        recommendations.append(f"{skill}: {guidance}")

    if not recommendations:
        recommendations.append(
            "No missing skills were identified by the current skill "
            "dictionary. Review the job responsibilities and build "
            "a project that demonstrates the relevant requirements."
        )

    return recommendations
