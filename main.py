from database import get_db_connection, create_users_table
import auth

def main():
    conn = get_db_connection()
    create_users_table(conn)

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            auth.register_user(conn)
        elif choice == '2':
            auth.login_user(conn)
        elif choice == '3':
            auth.logout_user(conn)
        elif choice == '4':
            auth.change_password(conn)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    conn.close()

if __name__ == "__main__":
    main()
