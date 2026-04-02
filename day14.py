# Password Generator + Saver

import random
import string
import os

FILE_NAME = "passwords.txt"

def show_menu():
    print("\n===== PASSWORD MANAGER =====")
    print("1. Generate Password")
    print("2. View Saved Passwords")
    print("3. Search Password")
    print("4. Delete All Passwords")
    print("5. Exit")

def generate_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    print("Generated Password:", password)

    save = input("Do you want to save it? (yes/no): ")
    if save.lower() == "yes":
        website = input("Enter website/app name: ")
        save_password(website, password)

def save_password(website, password):
    with open(FILE_NAME, "a") as file:
        file.write(website + "," + password + "\n")
    print("Password saved successfully!")

def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("No saved passwords.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No passwords found.")
        return

    print("\nSaved Passwords:")
    for i, line in enumerate(data):
        site, pwd = line.strip().split(",")
        print(f"{i+1}. {site} → {pwd}")

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
                print(f"Found: {site} → {pwd}")
                found = True

    if not found:
        print("Password not found.")

def delete_all():
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("All passwords deleted.")
    else:
        print("Cancelled.")

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
            delete_all()
        elif choice == "5":
            print("Goodbye! 🔐")
            break
        else:
            print("Invalid choice.")

# Initialize file
def initialize():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

# Extra feature: count saved passwords
def count_passwords():
    if not os.path.exists(FILE_NAME):
        return 0
    with open(FILE_NAME, "r") as file:
        return len(file.readlines())

# Run program
if __name__ == "__main__":
    initialize()
    print(f"Loaded {count_passwords()} saved passwords.")
    main()


    # This code implements a simple password manager that allows users to generate, save, view, search, and delete passwords. The passwords are stored in a text file for persistence. The program provides a menu-driven interface for easy navigation and includes error handling for edge cases such as empty files or invalid inputs.