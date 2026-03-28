# Expense Tracker with File Handling

import os

FILE_NAME = "expenses.txt"

def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete All Expenses")
    print("5. Exit")

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + amount + "\n")

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No expenses available.")
        return

    print("\nYour Expenses:")
    for i, line in enumerate(data):
        name, amount = line.strip().split(",")
        print(f"{i+1}. {name} - ₹{amount}")

def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, amount = line.strip().split(",")
            total += float(amount)

    print(f"\nTotal Expense: ₹{total}")

def delete_all():
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("All expenses deleted.")
    else:
        print("Cancelled.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            delete_all()
        elif choice == "5":
            print("Goodbye! 💸")
            break
        else:
            print("Invalid choice.")

# Extra feature: initialize file
def initialize():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

# Extra feature: count expenses
def count_expenses():
    if not os.path.exists(FILE_NAME):
        return 0
    with open(FILE_NAME, "r") as file:
        return len(file.readlines())

# Run program
if __name__ == "__main__":
    initialize()
    print(f"Loaded {count_expenses()} expenses.")
    main()

 # Quiz Game with Custom Questions
 # # Quiz Game with Custom Questions   