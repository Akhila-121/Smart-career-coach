import streamlit as st
from resume_parser import parse_resume
from match_engine import match_jobs
from utils.db_utils import get_learning_resources

st.set_page_config(page_title="Smart Career Coach", layout="centered")

# Session state to control app flow
if "step" not in st.session_state:
    st.session_state.step = 1
if "skills" not in st.session_state:
    st.session_state.skills = []
if "matched_jobs" not in st.session_state:
    st.session_state.matched_jobs = []

# Step 1: Upload Resume
if st.session_state.step == 1:
    st.title("📄 Upload Your Resume")
    uploaded_file = st.file_uploader("Choose your resume file", type=["pdf", "docx", "txt", "jpg", "png"])

    if uploaded_file:
        with st.spinner("🔍 Extracting skills..."):
            parsed = parse_resume(uploaded_file)
            st.session_state.skills = parsed["skills"]
            st.session_state.matched_jobs = match_jobs(st.session_state.skills)
            st.session_state.step = 2
            st.rerun()

# Step 2: Show Job Matches
elif st.session_state.step == 2:
    st.title("🎯 Matched Job Roles")

    if st.session_state.skills:
        st.subheader("🧠 Extracted Skills")
        st.success(", ".join(st.session_state.skills))

        for job in st.session_state.matched_jobs[:5]:
            st.markdown(f"### ✅ {job['role_name']}")
            st.progress(job["match_percent"] / 100)
            st.caption(f"Match: **{job['match_percent']}%**")
            st.markdown(f"🛠️ Required Skills: `{', '.join(job['required_skills'])}`")
            st.markdown("---")

        if st.button("📘 Show Recommendations"):
            st.session_state.step = 3
            st.rerun()
    else:
        st.warning("⚠️ No skills found. Please go back and upload a valid resume.")
    
    st.button("🔙 Back to Upload", on_click=lambda: st.session_state.update(step=1))

# Step 3: Show Course Recommendations
elif st.session_state.step == 3:
    st.title("📘 Recommended Learning Resources")

    if st.session_state.skills:
        st.subheader("🧠 Based on Your Extracted Skills")

        found_any = False
        for skill in st.session_state.skills:
            resources = get_learning_resources(skill)
            if resources:
                found_any = True
                st.markdown(f"### 📌 For Skill: **{skill.title()}**")
                for course in resources:
                    st.markdown(f"- [{course[0]}]({course[1]})")
                st.markdown("---")

        if not found_any:
            st.warning("⚠️ No matching resources found for your skills.")
    else:
        st.error("❌ No skills found to recommend courses for.")

    st.button("🔙 Back to Matches", on_click=lambda: st.session_state.update(step=2))
