import json
import os
from datetime import datetime

def load_deadlines():
    if not os.path.exists("deadlines.json"):
        return []

    with open("deadlines.json", "r") as f:
        return json.load(f)

def save_deadlines(deadlines):
    with open("deadlines.json", "w") as f:
        json.dump(deadlines, f, indent=4)

def add_task():
    title = input("Enter task title: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    # Validate date format
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print(" Invalid date format. Please use YYYY-MM-DD.")
        return

    email = input("Enter email address: ").strip()
    whatsapp = input("Enter WhatsApp number (with country code): ").strip()

    task = {
        "title": title,
        "due_date": due_date,
        "email": email,
        "whatsapp": whatsapp,
        "notified_days": []
    }

    deadlines = load_deadlines()
    deadlines.append(task)
    save_deadlines(deadlines)

    print(f" Task '{title}' added successfully!")

if __name__ == "__main__":
    add_task()
