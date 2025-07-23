import json
import os
from datetime import datetime
from plyer import notification
from notifier import send_deadline_alert
from email_notifier import send_email

def check_deadlines():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    deadlines_path = os.path.join(base_dir, "deadlines.json")

    with open(deadlines_path, "r") as f:
        deadlines = json.load(f)

    today = datetime.now().date()
    
    for task in deadlines:
        if "notified_days" not in task:
           task["notified_days"] = []

        due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        days_left = (due - today).days
        
        if days_left < 0:
           continue
        

        if days_left <= 3:
            # Windows notification
            notification.notify(
                title=f" Deadline Approaching: {task['title']}",
                message=f"{days_left} day(s) left (Due: {task['due_date']})",
                timeout=10
            )

            # Email notification
            subject = f"Deadline Reminder: {task['title']}"
            body = f"The task '{task['title']}' is due in {days_left} day(s) on {task['due_date']}."
            try:
                send_email(subject, body, "knav12mna@gmail.com")
            except Exception as e:
                print(f" Failed to send email for '{task['title']}': {e}")

        # WhatsApp/SMS alert only on days 3, 1, or 0 if not already sent
        if days_left in [3, 1, 0] and days_left not in task["notified_days"]:
            try:
                send_deadline_alert(task["title"], task["due_date"], task["phone"])
                task["notified_days"].append(days_left)
            except Exception as e:
                print(f" Failed to send SMS for '{task['title']}': {e}")

    # Update deadlines with new notified_days
    with open(deadlines_path, "w") as f:
        json.dump(deadlines, f, indent=4)

    # Log the check
    with open(os.path.join(base_dir, "log.txt"), "a") as log:
        log.write(f"Checked deadlines on {datetime.now()}\n")

if __name__ == "__main__":
    check_deadlines()
