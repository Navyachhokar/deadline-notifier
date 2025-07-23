from twilio.rest import Client
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
from_number = os.getenv("FROM_NUMBER")
to_number = os.getenv("TO_NUMBER")

client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        from_=from_number,
        body=" Hello! This is a test from your Deadline Manager!",
        to=to_number
    )
    print("✅ Message sent:", message.sid)
except Exception as e:
    error_message = f"[{datetime.now()}] ❌ SMS failed to '{to_number}' — {str(e)}\n"
    print(error_message)
    with open("log.txt", "a") as log:
        log.write(error_message)

