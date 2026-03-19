# Simple To-Do List Application
#to do list
tasks = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
  
def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Stay productive! 💪")
            break
        else:
            print("Invalid choice. Try again.")

# Extra feature: Preload some tasks
def preload_tasks():
    sample = ["Learn Python", "Practice DSA", "Build Project"]
    for t in sample:
        tasks.append({"task": t, "done": False})

# Extra feature: Count tasks
def task_summary():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    pending = total - done
    print(f"\nSummary: Total={total}, Done={done}, Pending={pending}")

# Run program
if __name__ == "__main__":
    preload_tasks()
    main()
    task_summary()
