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

def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("❌ No tasks found.")
        return

    print("\n📋 Current Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")

    try:
        idx = int(input("\nEnter the task number to delete: "))
        if 1 <= idx <= len(tasks):
            deleted = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"✅ Deleted task: {deleted['title']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    delete_task()
