import sqlite3

def get_db_connection():
    conn = sqlite3.connect("coplur500.db")
    return conn

def create_users_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE COLLATE NOCASE,
            password TEXT NOT NULL,
            is_logged_in INTEGER DEFAULT 0
        );
    ''')
    conn.commit()

def add_user(conn, username, password_hash):
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password_hash)
    )
    conn.commit()

def get_user(conn, username):
    cursor = conn.execute(
        "SELECT username, password, is_logged_in FROM users WHERE username = ? COLLATE NOCASE",
        (username,)
    )
    return cursor.fetchone()

def update_login_status(conn, username, status):
    conn.execute(
        "UPDATE users SET is_logged_in = ? WHERE username = ? COLLATE NOCASE",
        (status, username)
    )
    conn.commit()

def update_password(conn, username, new_password_hash):
    conn.execute(
        "UPDATE users SET password = ? WHERE username = ? COLLATE NOCASE",
        (new_password_hash, username)
    )
    conn.commit()
