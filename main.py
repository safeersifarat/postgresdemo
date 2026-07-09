from crud.insert import insert_user
from crud.update import update_user
from crud.delete import delete_user

def menu():
    while True:
        print("\n===== User Management =====")
        print("1. Insert User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = int(input("Enter ID: "))
            username = input("Enter Username: ")
            insert_user(user_id, username)

        elif choice == "2":
            user_id = int(input("Enter ID: "))
            username = input("Enter New Username: ")
            update_user(user_id, username)

        elif choice == "3":
            user_id = int(input("Enter ID: "))
            delete_user(user_id)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
menu()