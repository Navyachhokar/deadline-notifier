import json
import datetime
import sys
from plyer import notification  #  Using plyer now
import scheduler

scheduler.check_deadlines()


# Logs all print() to log.txt
sys.stdout = open("log.txt", "a", encoding="utf-8")

print("==== Task Ran ====")

def show_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=10  # seconds
        )
    except Exception as e:
        print(f"Notification error: {e}")  #  Log error if notification fails

def get_upcoming_deadlines(days_ahead=3):
    try:
        with open("deadlines.json", "r") as file:
            deadlines = json.load(file)
    except FileNotFoundError:
        print("deadlines.json not found.")
        return []

    today = datetime.date.today()
    upcoming = []

    for task in deadlines:
        due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        if 0 <= (due_date - today).days <= days_ahead:
            upcoming.append(task)

    return upcoming

if __name__ == "__main__":
    upcoming = get_upcoming_deadlines()
    if upcoming:
        for task in upcoming:
            msg = f"{task['title']} - Due: {task['due_date']}"
            print(f" {msg}")
            show_notification("Upcoming Deadline", msg)
    else:
        print(" No tasks today.")


# import json
# import datetime
# from win10toast import ToastNotifier  #  Correct import
# import sys

# # Logs all print() to log.txt
# sys.stdout = open("log.txt", "a", encoding="utf-8")

# print("==== Task Ran ====")

# def show_notification(title, message):
#     try:
#         toaster = ToastNotifier()
#         toaster.show_toast(title, message, duration=10, threaded=True)
#     except Exception as e:
#         print(f"Notification error: {e}")  # ✅ Log error if toast fails

# def get_upcoming_deadlines(days_ahead=3):
#     try:
#         with open("deadlines.json", "r") as file:
#             deadlines = json.load(file)
#     except FileNotFoundError:
#         print("deadlines.json not found.")
#         return []

#     today = datetime.date.today()
#     upcoming = []

#     for task in deadlines:
#         due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
#         if 0 <= (due_date - today).days <= days_ahead:
#             upcoming.append(task)

#     return upcoming

# if __name__ == "__main__":
#     upcoming = get_upcoming_deadlines()
#     for task in upcoming:
#         msg = f"{task['title']} - Due: {task['due_date']}"
#         print(f" {msg}")
#         show_notification(" Upcoming Deadline", msg)




# import schedule
# import time
# from scheduler import check_deadlines

# # Schedule the task to run every day at 9:00 AM
# schedule.every(10).seconds.do(check_deadlines)


# print(" Deadline checker is running...")

# while True:
#     schedule.run_pending()
#     time.sleep(60)
