import sqlite3

def insert_sample_courses():
    conn = sqlite3.connect("careercoach.db")
    cursor = conn.cursor()

    # Ensure table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill TEXT NOT NULL,
            course_title TEXT,
            course_link TEXT
        )
    ''')

    sample_data = [
        ("Python", "Python for Everybody - Coursera", "https://www.coursera.org/specializations/python"),
        ("SQL", "SQL for Data Analysis - Udemy", "https://www.udemy.com/course/sql-for-data-analysis/"),
        ("Excel", "Excel Skills for Business - Coursera", "https://www.coursera.org/specializations/excel"),
        ("Power BI", "Getting Started with Power BI - Microsoft Learn", "https://learn.microsoft.com/en-us/training/paths/get-started-power-bi/"),
        ("Machine Learning", "Machine Learning - Coursera (Andrew Ng)", "https://www.coursera.org/learn/machine-learning"),
        ("Data Visualization", "Data Visualization with Tableau - Coursera", "https://www.coursera.org/specializations/data-visualization"),
        ("Data Analysis", "Data Analyst Career Path - DataCamp", "https://www.datacamp.com/tracks/data-analyst-with-python"),
        ("Pandas", "Data Manipulation with Pandas - DataCamp", "https://www.datacamp.com/courses/data-manipulation-with-pandas"),
        ("Numpy", "Intro to Numpy - W3Schools", "https://www.w3schools.com/python/numpy_intro.asp"),
        ("PowerPoint", "PowerPoint for Beginners - Udemy", "https://www.udemy.com/course/powerpoint-for-beginners/")
    ]

    cursor.executemany("INSERT INTO courses (skill, course_title, course_link) VALUES (?, ?, ?)", sample_data)
    conn.commit()
    conn.close()
    print("✅ Sample learning resources inserted successfully.")

# Run it
if __name__ == "__main__":
    insert_sample_courses()
