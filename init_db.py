import sqlite3

# Connect to DB (or create if it doesn't exist)
conn = sqlite3.connect("career_coach.db")
cursor = conn.cursor()

# Create the learning_resources table
cursor.execute("""
CREATE TABLE IF NOT EXISTS learning_resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL
)
""")

# Sample data to insert (you can add more)
sample_data =sample_data = [
    # Data Analyst
    ("Data Analyst", "Google Data Analytics Certificate", "https://coursera.org/professional-certificates/google-data-analytics"),
    ("Data Analyst", "Excel for Data Analysis", "https://coursera.org/learn/excel-data-analytics"),
    ("Data Analyst", "SQL for Data Science", "https://coursera.org/learn/sql-for-data-science"),

    # Cloud Engineer
    ("Cloud Engineer", "Cloud Computing Basics", "https://coursera.org/learn/cloud-computing"),
    ("Cloud Engineer", "AWS Cloud Practitioner Essentials", "https://www.aws.training/Details/Curriculum?id=20685"),
    ("Cloud Engineer", "Google Cloud Fundamentals", "https://coursera.org/learn/gcp-fundamentals"),

    # System Application Developer
    ("System Application Developer", "Java Programming Masterclass", "https://udemy.com/course/java-the-complete-java-developer-course"),
    ("System Application Developer", "C# Fundamentals for Beginners", "https://udemy.com/course/csharp-tutorial-for-beginners/"),

    # Package Developer
    ("Package Developer", "SAP Package Development Basics", "https://learning.sap.com/learning-journeys/"),
    ("Package Developer", "SAP ABAP Development for Beginners", "https://udemy.com/course/sap-abap-programming-for-beginners/"),

    # Web Developer
    ("Web Developer", "The Web Developer Bootcamp", "https://udemy.com/course/the-web-developer-bootcamp/"),
    ("Web Developer", "HTML/CSS Crash Course", "https://freecodecamp.org/learn"),

    # AI Engineer
    ("AI Engineer", "AI For Everyone - Andrew Ng", "https://coursera.org/learn/ai-for-everyone"),
    ("AI Engineer", "Machine Learning Specialization", "https://coursera.org/specializations/machine-learning-introduction"),

    # UI/UX Designer
    ("UI/UX Designer", "Google UX Design Certificate", "https://coursera.org/professional-certificates/google-ux-design"),
    ("UI/UX Designer", "Figma for Beginners", "https://youtube.com/playlist?list=PLWlUJU11tp4fVdN0Z3EByXfUzcoEnnz2s"),

    # Cybersecurity Analyst
    ("Cybersecurity Analyst", "IBM Cybersecurity Analyst Certificate", "https://coursera.org/professional-certificates/ibm-cybersecurity-analyst"),
    ("Cybersecurity Analyst", "CompTIA Security+ Training", "https://udemy.com/course/comptia-security-certification/"),

    # Database Administrator
    ("Database Administrator", "Database Foundations - Oracle", "https://oracle.com/education/"),
    ("Database Administrator", "SQL and Database Management", "https://coursera.org/specializations/learn-sql-database"),

    # DevOps Engineer
    ("DevOps Engineer", "Introduction to DevOps", "https://coursera.org/learn/devops-culture-and-mindset"),
    ("DevOps Engineer", "CI/CD with Jenkins", "https://udemy.com/course/jenkins-tutorial-for-beginners/"),

    # Business Analyst
    ("Business Analyst", "Business Analysis & Process Management", "https://coursera.org/learn/business-process-management"),
    ("Business Analyst", "Business Analytics Specialization", "https://coursera.org/specializations/business-analytics"),

    # Mobile App Developer
    ("Mobile App Developer", "Android App Development with Kotlin", "https://developer.android.com/courses"),
    ("Mobile App Developer", "iOS App Development with Swift", "https://developer.apple.com/learn/curriculum/")
]


# Insert sample data
cursor.executemany("INSERT INTO learning_resources (role, title, url) VALUES (?, ?, ?)", sample_data)

# Save and close
conn.commit()
conn.close()

print("✅ Database created and sample data inserted.")
