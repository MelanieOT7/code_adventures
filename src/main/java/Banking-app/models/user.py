from models.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    conn = get_connection()
    c = conn.cursor()
    hashed = generate_password_hash(password)
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Username already exists"
    conn.close()
    return True, "User created"

def verify_user(username, password):
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    if not row:
        return False, "User not found"
    if check_password_hash(row["password"], password):
        return True, row["id"]
    return False, "Incorrect password"
