import sqlite3

def create_connection(db_file="careercoach.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("✅ SQLite connection is ready.")
    except sqlite3.Error as e:
        print(f"❌ Error: {e}")
    return conn

def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS job_roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_name TEXT NOT NULL,
                required_skills TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                skill TEXT NOT NULL,
                course_title TEXT,
                course_link TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                current_skills TEXT,
                goal_role TEXT,
                missing_skills TEXT,
                recommended_courses TEXT
            )
        ''')

        conn.commit()
        print("✅ Tables created successfully.")
    except sqlite3.Error as e:
        print(f"❌ Table creation error: {e}")

def get_learning_resources(skill, db_path="careercoach.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT course_title, course_link
        FROM courses
        WHERE LOWER(skill) LIKE LOWER(?)
    """
    cursor.execute(query, (f"%{skill}%",))
    results = cursor.fetchall()
    conn.close()
    return results
