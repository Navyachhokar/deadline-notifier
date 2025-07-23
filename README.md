# 📅 Deadline Notifier CLI

A simple command-line task and deadline manager with daily reminders and email notifications.

---

## 🚀 Features

- 📋 Add, view, edit, or delete tasks with deadlines.
- ✅ Mark tasks as completed.
- 📨 Get daily reminders via email.
- 📦 Auto-archive completed tasks.
- 📅 Daily scheduled runner using Python's `schedule`.

---

## 🛠️ Technologies Used

- Python 3
- `smtplib` for sending emails
- `schedule` for task scheduling
- `.env` for storing sensitive data (email & password)

---

## 📂 File Structure

.
├── add_task.py # Add new task to deadlines.json
├── archive_tasks.py # Archive completed tasks
├── completed.json # Stores completed tasks
├── daily_runner.py # Main script that checks and notifies daily
├── deadlines.json # Stores all pending tasks
├── delete_task.py # Delete a specific task
├── edit_task.py # Edit existing tasks
├── email_notifier.py # Sends email notifications
├── file_list.txt # For listing file names (optional)
├── list_files.py # Script to list files in the project
├── log.txt # Error logging file
├── notifier.py # Notification logic
├── scheduler.py # Scheduling wrapper
├── send_message.py # Text message support (if integrated)
├── test_notifier.py # For testing notification logic
├── view_completed.py # View completed tasks
├── view_tasks.py # View all pending tasks
├── .env # Environment variables (not pushed)
├── .gitignore # Ignore sensitive/generated files

---

## 🧪 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/Navyachhokar/deadline-notifier.git
   cd deadline-manager
