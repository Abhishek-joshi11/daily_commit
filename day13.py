# Calculator with History

import os

FILE_NAME = "history.txt"

def show_menu():
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")

def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except:
        print("Invalid input.")
        return None, None

def save_history(entry):
    with open(FILE_NAME, "a") as file:
        file.write(entry + "\n")

def add():
    a, b = get_numbers()
    if a is None: return
    result = a + b
    entry = f"{a} + {b} = {result}"
    print("Result:", result)
    save_history(entry)

def subtract():
    a, b = get_numbers()
    if a is None: return
    result = a - b
    entry = f"{a} - {b} = {result}"
    print("Result:", result)
    save_history(entry)

def multiply():
    a, b = get_numbers()
    if a is None: return
    result = a * b
    entry = f"{a} * {b} = {result}"
    print("Result:", result)
    save_history(entry)

def divide():
    a, b = get_numbers()
    if a is None: return
    if b == 0:
        print("Cannot divide by zero.")
        return
    result = a / b
    entry = f"{a} / {b} = {result}"
    print("Result:", result)
    save_history(entry)

def view_history():
    if not os.path.exists(FILE_NAME):
        print("No history found.")
        return
    with open(FILE_NAME, "r") as file:
        data = file.readlines()
    if not data:
        print("History is empty.")
        return
    print("\nCalculation History:")
    for line in data:
        print(line.strip())

def clear_history():
    confirm = input("Clear all history? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("History cleared.")
    else:
        print("Cancelled.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            view_history()
        elif choice == "6":
            clear_history()
        elif choice == "7":
            print("Goodbye! 🧮")
            break
        else:
            print("Invalid choice.")

# Initialize file
def initialize():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

# Run program
if __name__ == "__main__":
    initialize()
    main()
    # This code implements a simple calculator with a history feature. Users can perform basic arithmetic operations and view or clear their calculation history. The history is stored in a text file, allowing for persistence across sessions.

