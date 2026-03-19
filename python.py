import random
import string

def show_menu():
    print("\n==== PASSWORD GENERATOR ====")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

def generate_password():
    print("\nChoose password complexity:")
    print("1. Weak (letters only)")
    print("2. Medium (letters + numbers)")
    print("3. Strong (letters + numbers + symbols)")

    choice = input("Enter choice: ")
    length = int(input("Enter password length: "))

    if choice == "1":
        chars = string.ascii_letters
    elif choice == "2":
        chars = string.ascii_letters + string.digits
    elif choice == "3":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice.")
        return

    password = ""
    for _ in range(length):
        password += random.choice(chars)

    print("Generated Password:", password)

def check_strength():
    password = input("\nEnter password to check: ")

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    print("\nPassword Analysis:")
    print(f"Length: {length}")
    print(f"Uppercase: {has_upper}")
    print(f"Lowercase: {has_lower}")
    print(f"Digits: {has_digit}")
    print(f"Symbols: {has_symbol}")

    if score <= 2:
        print("Strength: Weak ❌")
    elif score == 3 or score == 4:
        print("Strength: Medium ⚠️")
    else:
        print("Strength: Strong ✅")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            check_strength()
        elif choice == "3":
            print("Goodbye! 🔐")
            break
        else:
            print("Invalid choice.")

# Extra feature: suggest strong password
def suggest_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(12))
    print("\nSuggested Strong Password:", password)

# Run program
if __name__ == "__main__":
    suggest_password()
    main()