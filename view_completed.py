import json

def view_completed_tasks():
    try:
        with open('completed.json', 'r') as f:
            completed = json.load(f)
    except FileNotFoundError:
        print("❌ completed.json not found.")
        return

    if not completed:
        print("ℹ️ No completed tasks found.")
        return

    print("\n✅ Completed Tasks:")
    print("-" * 40)
    for i, task in enumerate(completed, start=1):
        print(f"{i}. {task['title']} (Due: {task['due_date']})")
    print("-" * 40)

if __name__ == "__main__":
    view_completed_tasks()
