import re
import hashlib
import getpass
from database import add_user, get_user, update_login_status, update_password


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_username(username):
    if len(username) < 3 or len(username) > 20:
        return False
    pattern = r'^[A-Za-z0-9_.-]+$'  # Allow letters, numbers, _, -, .
    if not re.match(pattern, username):
        return False
    return True


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


def register_user(conn):
    print("::: Welcome to the register section, please register to the portal :::\n")
    username = input("Enter the username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if not is_valid_username(username):
        print("Username must be 3-20 characters long and can include letters, digits, underscore (_), dot (.), and hyphen (-).")
        return
    existing_user = get_user(conn, username)
    if existing_user:
        print("SORRY!! Username already exists.")
        return
    password = getpass.getpass("Please input your password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return
    if not is_valid_password(password):
        print("Password must be at least 8 characters long and include uppercase, lowercase letters, and digits.")
        return
    hashed = hash_password(password)
    add_user(conn, username, hashed)
    print("Congratulations, user signed up successfully!")


def login_user(conn):
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()
    user = get_user(conn, username)
    if not user:
        print("User not found.")
        return
    stored_username, stored_hash, logged_in = user
    if logged_in:
        print("User is already logged in.")
        return
    if hash_password(password) == stored_hash:
        update_login_status(conn, stored_username, 1)
        print("Logged in successfully.")
    else:
        print("Incorrect password.")


def logout_user(conn):
    username = input("Username: ").strip()
    password = getpass.getpass("Current password: ").strip()
    user = get_user(conn, username)
    if not user:
        print("User not found.")
        return
    stored_username, stored_hash, logged_in = user
    if not logged_in:
        print("User is not logged in.")
        return
    if hash_password(password) == stored_hash:
        update_login_status(conn, stored_username, 0)
        print("Logged out successfully.")
    else:
        print("Incorrect password.")


def change_password(conn):
    username = input("Username: ").strip()
    user = get_user(conn, username)
    if not user:
        print("User not found.")
        return
    stored_username, stored_hash, _ = user
    current_password = getpass.getpass("Current password: ").strip()
    if hash_password(current_password) != stored_hash:
        print("Current password is incorrect.")
        return
    new_password = getpass.getpass("Enter new password: ").strip()
    if not new_password:
        print("New password cannot be empty.")
        return
    if not is_valid_password(new_password):
        print("New password must be at least 8 characters long and include uppercase, lowercase letters, and digits.")
        return
    update_password(conn, stored_username, hash_password(new_password))
    print("Password updated successfully.")
