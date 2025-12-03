import os
import json

FILENAME = "tasks.json"

# ------------ Load tasks from file ------------
todo_list = []

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        try:
            todo_list = json.load(file)
        except:
            todo_list = []

# ------------ Save tasks to file ------------
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(todo_list, file, indent=4)

# ------------ Main program ------------
while True:
    print("\n=== To-Do List Menu ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark as completed")
    print("5. Exit")

    choice = input("Choose an option: ")

    # View tasks
    if choice == "1":
        if len(todo_list) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todo_list, 1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['title']} [{status}]")

    # Add task
    elif choice == "2":
        title = input("Enter new task: ")
        todo_list.append({"title": title, "completed": False})
        save_tasks()
        print(f"Task '{title}' added.")

    # Remove task
    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove!")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task['title']}")

            index = int(input("Enter task number to remove: "))

            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                save_tasks()
                print(f"Task '{removed['title']}' removed.")
            else:
                print("Invalid number!")

    # Mark as completed
    elif choice == "4":
        if len(todo_list) == 0:
            print("No tasks to mark!")
        else:
            for i, task in enumerate(todo_list, 1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['title']} [{status}]")

            index = int(input("Enter task number to mark as completed: "))

            if 1 <= index <= len(todo_list):
                todo_list[index - 1]["completed"] = True
                save_tasks()
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    # Exit
    elif choice == "5":
        print("Goodbye! Your tasks are saved.")
        break

    else:
        print("Invalid choice! Try again.")
