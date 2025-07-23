import json
from datetime import datetime

def archive_past_tasks():
    try:
        with open('deadlines.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("❌ deadlines.json not found.")
        return

    today = datetime.now().date()
    upcoming, completed = [], []

    for task in tasks:
        due_date = datetime.strptime(task['due_date'], "%Y-%m-%d").date()
        if due_date < today:
            completed.append(task)
        else:
            upcoming.append(task)

    with open('deadlines.json', 'w') as f:
        json.dump(upcoming, f, indent=4)

    if completed:
        try:
            with open('completed.json', 'r') as f:
                completed_existing = json.load(f)
        except FileNotFoundError:
            completed_existing = []

        completed_all = completed_existing + completed
        with open('completed.json', 'w') as f:
            json.dump(completed_all, f, indent=4)

        print(f"✅ Archived {len(completed)} task(s) to completed.json.")
    else:
        print("ℹ️ No past tasks to archive.")

# Run the function
if __name__ == "__main__":
    archive_past_tasks()
