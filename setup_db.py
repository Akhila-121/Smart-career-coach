from utils.db_utils import create_connection, create_tables

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_tables(conn)
        conn.close()
def insert_sample_data(conn):
    cursor = conn.cursor()

   

    # Insert sample job roles (fresher-focused)
    job_roles = [
        ("Data Analyst", "Excel, SQL, Python, Power BI, Statistics"),
        ("System Application Software Developer", "C++, Java, OOPs, Operating Systems"),
        ("Package Developer", "SAP, ABAP, Java, .NET"),
        ("Cloud Engineer", "AWS, Azure, Linux, Networking"),
        ("Frontend Developer", "HTML, CSS, JavaScript, React"),
        ("Backend Developer", "Python, Django, APIs, SQL"),
        ("AI/ML Engineer", "Python, Machine Learning, Deep Learning, TensorFlow"),
        ("Cybersecurity Analyst", "Networking, Firewalls, Security Tools, Risk Assessment"),
        ("DevOps Engineer", "Linux, CI/CD, Docker, Jenkins, AWS"),
        ("QA/Test Engineer", "Manual Testing, Automation Testing, Selenium, JUnit"),
        ("Business Analyst", "Excel, SQL, Communication Skills, Requirement Analysis"),
        ("Technical Support Engineer", "Troubleshooting, Hardware, Software, Customer Support"),
        ("Mobile App Developer", "Java, Kotlin, Flutter, Android SDK"),
        ("Database Developer", "SQL, PL/SQL, Oracle, DBMS Concepts")
    ]

    cursor.executemany('''
        INSERT INTO job_roles (role_name, required_skills)
        VALUES (?, ?)
    ''', job_roles)

    # Insert sample courses
    courses = [
        ("Python", "Python for Everybody", "https://www.coursera.org/specializations/python"),
        ("Machine Learning", "ML Crash Course by Google", "https://developers.google.com/machine-learning/crash-course"),
        ("SQL", "SQL for Data Science", "https://www.coursera.org/learn/sql-for-data-science"),
        ("React", "React - The Complete Guide", "https://www.udemy.com/course/react-the-complete-guide/"),
        ("Django", "Django for Beginners", "https://www.djangoproject.com/start/"),
        ("AWS", "AWS Cloud Practitioner Essentials", "https://www.aws.training/Details/Curriculum?id=20685"),
        ("Java", "Java Programming Masterclass", "https://www.udemy.com/course/java-the-complete-java-developer-course/"),
        ("Cybersecurity", "Introduction to Cyber Security", "https://www.futurelearn.com/courses/introduction-to-cyber-security"),
        ("Excel", "Excel Skills for Business", "https://www.coursera.org/specializations/excel"),
        ("Flutter", "Flutter Development Bootcamp", "https://www.udemy.com/course/flutter-bootcamp-with-dart/")
    ]

    cursor.executemany('''
        INSERT INTO courses (skill, course_title, course_link)
        VALUES (?, ?, ?)
    ''', courses)

    conn.commit()
    print("✅ Sample data inserted.")

# Main logic
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_tables(conn)
        insert_sample_data(conn)
        conn.close()
