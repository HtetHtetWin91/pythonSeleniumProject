import sqlite3


def get_user_by_email(email):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Use parameterized queries to prevent SQL injection
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

        result = cursor.fetchone()
        return result

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        conn.close()  # Ensures the connection is always closed

    return None
