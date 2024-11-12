# To-Do List Application (Command Line)

import os

# Define the To-Do List class
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added to your to-do list.")

    def remove_task(self, task_number):
        """Remove a task from the list by its number."""
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Task '{removed_task['task']}' removed from your to-do list.")
        else:
            print("Invalid task number. Please try again.")

    def mark_done(self, task_number):
        """Mark a task as completed."""
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["done"] = True
            print(f"Task '{self.tasks[task_number]['task']}' marked as done.")
        else:
            print("Invalid task number. Please try again.")

    def list_tasks(self):
        """List all tasks with their status."""
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i + 1}. {task['task']} - {status}")

    def clear_tasks(self):
        """Clear all tasks."""
        self.tasks = []
        print("All tasks have been removed from your to-do list.")

# Function to display the menu and get user choice
def show_menu():
    print("\n--- To-Do List ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Clear all tasks")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

# Main program loop
def main():
    todo_list = TodoList()

    while True:
        choice = show_menu()

        if choice == "1":
            todo_list.list_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.list_tasks()
            try:
                task_number = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.list_tasks()
            try:
                task_number = int(input("Enter the task number to mark as done: ")) - 1
                todo_list.mark_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            todo_list.clear_tasks()
        elif choice == "6":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
