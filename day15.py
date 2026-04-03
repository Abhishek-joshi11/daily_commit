# Login & Signup System

import os

FILE_NAME = "users.txt"

def show_menu():
    print("\n===== AUTH SYSTEM =====")
    print("1. Signup")
    print("2. Login")
    print("3. View Users")
    print("4. Exit")

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if user_exists(username):
        print("Username already exists!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Signup successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not os.path.exists(FILE_NAME):
        print("No users found. Please signup first.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print("Login successful! 🎉")
                return

    print("Invalid credentials!")

def user_exists(username):
    if not os.path.exists(FILE_NAME):
        return False

    with open(FILE_NAME, "r") as file:
        for line in file:
            u, _ = line.strip().split(",")
            if u == username:
                return True
    return False

def view_users():
    if not os.path.exists(FILE_NAME):
        print("No users found.")
        return

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    if not users:
        print("No users available.")
        return

    print("\nRegistered Users:")
    for i, line in enumerate(users):
        u, _ = line.strip().split(",")
        print(f"{i+1}. {u}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            view_users()
        elif choice == "4":
            print("Goodbye! 🔒")
            break
        else:
            print("Invalid choice.")

# Initialize file
def initialize():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

# Extra feature: count users
def count_users():
    if not os.path.exists(FILE_NAME):
        return 0
    with open(FILE_NAME, "r") as file:
        return len(file.readlines())

# Run program
if __name__ == "__main__":
    initialize()
    print(f"Loaded {count_users()} users.")
    main()