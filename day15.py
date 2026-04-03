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

# Password Manager
# This program allows users to generate, view, search, and delete passwords for different websites. Passwords are stored in a local file for simplicity.
#   
#
jfnjnf
import os
import random   

FILE_NAME = "passwords.txt"
def show_menu():
    print("\n===== PASSWORD MANAGER =====")
    print("1. Generate Password")
    print("2. View Saved Passwords")
    print("3. Search Password")
    print("4. Delete All Passwords")
    print("5. Exit")    

def generate_password():
    website = input("Enter website: ")
    length = int(input("Enter password length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(length))

    with open(FILE_NAME, "a") as file:
        file.write(website + "," + password + "\n")

    print(f"Generated password for {website}: {password}")

def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("No saved passwords.")
        return

    print("\nSaved Passwords:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            site, pwd = line.strip().split(",")
            print(f"{site} → {pwd}")
def search_password():
    website = input("Enter website to search: ")
    if not os.path.exists(FILE_NAME):
        print("No saved passwords.")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            site, pwd = line.strip().split(",")
            if site.lower() == website.lower():
                print(f"Password for {site}: {pwd}")
                found = True
                break

    if not found:
        print("Password not found for that website.")
def delete_passwords():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("All passwords deleted.")
    else:
        print("No passwords to delete.")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_passwords()
        elif choice == "5":
            print("Goodbye! 🔒")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()

