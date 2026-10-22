
"""Extract technical skills from resume and job description text."""

import json
import re
from pathlib import Path

SKILLS_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "skills_dictionary.json"
)

DEFAULT_SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "natural language processing",
    "scikit-learn",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "excel",
    "power bi",
    "tableau",
    "data analysis",
    "data visualization",
    "statistics",
    "computer vision",
    "git",
    "streamlit",
    "flask",
    "java",
    "c++",
    "aws",
    "docker",
    "generative ai",
    "large language models",
]


def load_skills() -> list[str]:
    """Load skills from JSON, falling back to built-in defaults."""
    if SKILLS_FILE.exists():
        try:
            with SKILLS_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, list):
                return [item for item in data if isinstance(item, str)]

            if isinstance(data, dict):
                return [
                    item
                    for item in data.keys()
                    if isinstance(item, str)
                ]
        except (json.JSONDecodeError, OSError):
            pass

    return DEFAULT_SKILLS.copy()


def extract_skills(text: str) -> list[str]:
    """Return canonical skill names found in the supplied text."""
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    normalized = text.lower()
    found = []

    aliases = {
        "machine learning": ["machine learning", "machine-learning"],
        "natural language processing": [
            "natural language processing",
            "nlp",
        ],
        "scikit-learn": ["scikit-learn", "scikit learn", "sklearn"],
        "power bi": ["power bi", "powerbi"],
        "data analysis": ["data analysis", "data analytics"],
        "data visualization": [
            "data visualization",
            "data visualisation",
        ],
        "generative ai": ["generative ai", "genai"],
        "large language models": [
            "large language models",
            "large language model",
            "llms",
            "llm",
        ],
        "c++": ["c++"],
        "aws": ["aws", "amazon web services"],
    }

    for skill in load_skills():
        skill = skill.strip().lower()
        if not skill:
            continue

        candidates = aliases.get(skill, [skill])

        for candidate in candidates:
            pattern = r"(?<!\w)" + re.escape(candidate) + r"(?!\w)"
            if re.search(pattern, normalized):
                found.append(skill)
                break

    return sorted(set(found))
