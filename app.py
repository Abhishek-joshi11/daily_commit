# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")
    student = {"name": name, "age": age, "branch": branch}
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for i, student in enumerate(students):
        print(f"{i+1}. Name: {student['name']}, Age: {student['age']}, Branch: {student['branch']}")
    print()

def search_student():
    name = input("Enter name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:", student)
            found = True
    if not found:
        print("Student not found.\n")

def delete_student():
    name = input("Enter name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted.\n")
            return
    print("Student not found.\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

menu()
##2nd day learning
