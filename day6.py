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
def show_welcome():
    print("Welcome to the Password Strength Checker! 🔐")
# Extra feature: add custom question
def ask_question(question, options, answer):
    print("\n" + question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = input("Enter your choice: ")

    if choice.isdigit() and 1 <= int(choice) <= len(options):
        selected = options[int(choice) - 1]
        if selected == answer:
            print("Correct! ✅")
            return 1
        else:
            print("Wrong! ❌")
            return 0
    else:
        print("Invalid choice.")
        return 0        
def run_quiz():         
    score = 0
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Process Unit",
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Power Unit"
            ],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which data type is used for text in Python?",                        
            "options": ["int", "float", "str", "bool"],
            "answer": "str"

        },
        {
            "question": "What does RAM stand for?",
            "options": [
                "Random Access Memory",
                "Read Access Memory",
                "Run Access Memory",
                "Random Active Memory"
            ],
            "answer": "Random Access Memory"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "#", "<!-- -->", "--"],
            "answer": "#"
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["5", "6", "8", "9"],
            "answer": "8"
        }
    ]
    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])
    print(f"\nYour final score is: {score}/{len(questions)}")

