# Simple To-Do List CLI App

tasks = []

def view_tasks():
    # Display all tasks with numbers
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

def add_task():
    # Add a new task to the list
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Task cannot be empty.")

def remove_task():
    # Remove a task using its number
    view_tasks()
    if tasks:
        try:
            number = int(input("Enter the task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("That task number does not exist.")
        except ValueError:
            print("Please enter a valid number.")

# Keep showing the menu until the user chooses to quit
while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")