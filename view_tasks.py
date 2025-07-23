import json
from tabulate import tabulate

TASK_FILE = "deadlines.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("⚠️ No tasks found.")
        return

    table_data = []
    for idx, task in enumerate(tasks, start=1):
        table_data.append([idx, task["title"], task["due_date"]])

    print(tabulate(table_data, headers=["No.", "Task Title", "Due Date"], tablefmt="grid"))

if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
