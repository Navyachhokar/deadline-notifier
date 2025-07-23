from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send_deadline_alert(task_title, due_date, phone):
    try:
        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_TOKEN")
        from_number = os.getenv("FROM_NUMBER")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_="whatsapp:" + from_number,
            body=f" Reminder: Your task '{task_title}' is due on {due_date}!",
            to="whatsapp:" + phone
        )

        print(f"WhatsApp reminder sent for '{task_title}'")

    except Exception as e:
        print(f" Failed to send WhatsApp message for '{task_title}': {e}")
