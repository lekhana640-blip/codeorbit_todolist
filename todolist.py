"""
To-Do List CLI App - Version 2 (with file storage)
Tasks are saved to tasks.txt so they are still there next time you run it.
"""

TASKS_FILE = "tasks.txt"  # One task per line


def load_tasks():
    """Read tasks from the file. Return an empty list if the file doesn't exist yet."""
    tasks = []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task != "":  # Skip blank lines
                    tasks.append(task)
    except FileNotFoundError:
        # First run: no file yet, so just start with an empty list
        pass
    return tasks


def save_tasks(tasks):
    """Write all tasks to the file, one per line (overwrites old contents)."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    """Print the main menu."""
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def add_task(tasks):
    """Ask the user for a task, add it, and save."""
    new_task = input("Enter a new task: ").strip()

    if new_task == "":
        print("Task cannot be empty.")
        return

    tasks.append(new_task)
    save_tasks(tasks)  # Save right away so nothing is lost
    print(f"Added: {new_task}")


def view_tasks(tasks):
    """Show all tasks as a numbered list."""
    if len(tasks) == 0:
        print("Your to-do list is empty.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task(tasks):
    """Remove a task chosen by its number, then save."""
    if len(tasks) == 0:
        print("There are no tasks to remove.")
        return

    view_tasks(tasks)
    user_input = input("Enter the number of the task to remove: ").strip()

    if not user_input.isdigit():
        print("Please enter a valid number.")
        return

    task_number = int(user_input)

    if task_number < 1 or task_number > len(tasks):
        print(f"Task number must be between 1 and {len(tasks)}.")
        return

    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f"Removed: {removed_task}")


def main():
    """Load saved tasks, then run the menu until the user exits."""
    tasks = load_tasks()  # Start with whatever was saved last time

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()