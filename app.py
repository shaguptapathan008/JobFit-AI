
import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.matching_engine import match_resume_to_job
from src.reco import generate_recommendations


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="JobFit AI",
    page_icon="🎯",
    layout="wide",
)


# ---------------- CUSTOM STYLING ----------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b1020, #111a32);
        color: #f3f4f6;
    }

    h1, h2, h3, p, label {
        color: #f3f4f6;
    }

    div[data-testid="stMetric"] {
        background: #18243c;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #344563;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #7c3aed, #0891b2);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- HEADER ----------------

st.title("🎯 JobFit AI")
st.subheader("AI-powered Resume and Job Matching")

st.write(
    "Analyze your resume against a job description, "
    "discover skill gaps, and identify areas to improve."
)

st.divider()


# ---------------- RESUME UPLOAD ----------------

st.header("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume in PDF format",
    type=["pdf"],
    help="Upload a text-based PDF resume.",
)

resume_text = ""

if uploaded_file is not None:
    try:
        resume_bytes = uploaded_file.getvalue()
        resume_text = extract_text_from_pdf(resume_bytes)

        st.success(
            "Resume uploaded and text extracted successfully."
        )

        with st.expander("Preview extracted resume text"):
            st.text_area(
                "Extracted text",
                value=resume_text,
                height=200,
                disabled=True,
            )

    except (ValueError, TypeError) as exc:
        st.error(str(exc))


# ---------------- JOB DESCRIPTION ----------------

st.header("2. Enter the Job Description")

job_description = st.text_area(
    "Paste the complete job description",
    height=220,
    placeholder=(
        "Example: We are looking for a Python developer "
        "with SQL, machine learning, Pandas and Scikit-learn skills."
    ),
)


# ---------------- ANALYSIS ----------------

st.header("3. Analyze Your Match")

if st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True,
):

    if uploaded_file is None:
        st.warning("Please upload your resume PDF first.")

    elif not resume_text:
        st.warning(
            "Resume text could not be extracted. "
            "Please upload a readable, text-based PDF."
        )

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            with st.spinner("Analyzing your resume..."):
                result = match_resume_to_job(
                    resume_text,
                    job_description,
                )

                recommendations = generate_recommendations(
                    result
                )

            st.success("Analysis completed!")

            # ---------------- MATCHING RESULTS ----------------

            st.subheader("Your Matching Results")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Overall Match Score",
                f"{result['match_score']:.2f}%",
            )

            col2.metric(
                "Text Similarity",
                f"{result['text_similarity']:.2f}%",
            )

            col3.metric(
                "Skill Coverage",
                f"{result['skill_coverage']:.2f}%",
            )

            st.caption(
                "These scores are heuristic similarity measures, "
                "not probabilities of getting hired."
            )

            st.divider()

            # ---------------- MATCHED SKILLS ----------------

            st.subheader("✅ Matched Skills")

            if result["matched_skills"]:
                st.write(" · ".join(result["matched_skills"]))
            else:
                st.info(
                    "No recognised matching skills were found."
                )

            # ---------------- MISSING SKILLS ----------------

            st.subheader("📚 Skills to Develop")

            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.write(f"- {skill}")
            else:
                st.write(
                    "No missing skills were detected by the "
                    "current skill dictionary."
                )

            # ---------------- RECOMMENDATIONS ----------------

            st.subheader(
                "🎯 Personalized Learning Recommendations"
            )

            for recommendation in recommendations:
                st.markdown(f"- {recommendation}")

            # ---------------- DETAILED RESULTS ----------------

            with st.expander("View Detailed Analysis"):
                st.write("**Skills found in resume:**")
                st.json(result["resume_skills"])

                st.write("**Skills identified in job description:**")
                st.json(result["required_skills"])

                st.write("**Matched skills:**")
                st.json(result["matched_skills"])

                st.write("**Missing skills:**")
                st.json(result["missing_skills"])

        except Exception as exc:
            st.error(
                f"An error occurred during analysis: {exc}"
            )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "JobFit AI | Resume analysis and skill-gap assistance"
)
