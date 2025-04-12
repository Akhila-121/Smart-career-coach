import sqlite3

def get_all_jobs(db_path="careercoach.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, role_name, required_skills FROM job_roles")
    jobs = cursor.fetchall()
    conn.close()
    return jobs

def match_jobs(user_skills, db_path="careercoach.db"):
    user_skills = set([skill.lower() for skill in user_skills])
    matched = []

    for job in get_all_jobs(db_path):
        job_id, role_name, required_skills = job
        required_skills_set = set(skill.strip().lower() for skill in required_skills.split(","))
        match_count = len(user_skills & required_skills_set)
        match_percentage = (match_count / len(required_skills_set)) * 100 if required_skills_set else 0

        matched.append({
            "job_id": job_id,
            "role_name": role_name,
            "match_percent": round(match_percentage, 2),
            "required_skills": list(required_skills_set)
        })

    matched = sorted(matched, key=lambda x: x["match_percent"], reverse=True)
    return matched
