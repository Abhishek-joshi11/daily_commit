# Contact Book with File Handling

import os

FILE_NAME = "contacts.txt"

def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + phone + "\n")

    print("Contact saved successfully!")

def view_contacts():
    if not os.path.exists(FILE_NAME):
        print("No contacts found.")
        return

    with open(FILE_NAME, "r") as file:
        contacts = file.readlines()

    if not contacts:
        print("No contacts available.")
        return

    print("\nSaved Contacts:")
    for i, contact in enumerate(contacts):
        name, phone = contact.strip().split(",")
        print(f"{i+1}. {name} - {phone}")

def search_contact():
    name = input("Enter name to search: ")

    if not os.path.exists(FILE_NAME):
        print("No contacts found.")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            n, p = line.strip().split(",")
            if n.lower() == name.lower():
                print(f"Found: {n} - {p}")
                found = True

    if not found:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No contacts found.")
        return

    with open(FILE_NAME, "r") as file:
        contacts = file.readlines()

    with open(FILE_NAME, "w") as file:
        deleted = False
        for line in contacts:
            n, p = line.strip().split(",")
            if n.lower() != name.lower():
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting... 📞")
            break
        else:
            print("Invalid choice.")

# Extra feature: create file if not exists
def initialize():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

# Run program
if __name__ == "__main__":
    initialize()
    main()
    # Extra feature: add custom question
    # add_question(questions)