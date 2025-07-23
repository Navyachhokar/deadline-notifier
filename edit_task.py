import json
import os

def load_tasks():
    if not os.path.exists("deadlines.json"):
        return []
    with open("deadlines.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("deadlines.json", "w") as file:
        json.dump(tasks, file, indent=4)

def edit_task():
    tasks = load_tasks()

    if not tasks:
        print("❌ No tasks to edit.")
        return

    print("\n📋 Current Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")

    try:
        idx = int(input("\nEnter the task number to edit: "))
        if 1 <= idx <= len(tasks):
            task = tasks[idx - 1]
            print(f"✏️ Editing task: {task['title']}")

            new_title = input("Enter new title (leave empty to keep unchanged): ")
            new_date = input("Enter new due date (YYYY-MM-DD) (leave empty to keep unchanged): ")

            if new_title.strip():
                task['title'] = new_title.strip()
            if new_date.strip():
                task['due_date'] = new_date.strip()

            save_tasks(tasks)
            print("✅ Task updated successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    edit_task()
