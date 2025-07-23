import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(subject, body, to_email):
    from_email = os.getenv("EMAIL_ID")
    app_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, app_password)
            server.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        error_message = f"[{datetime.now()}] ❌ Email failed to '{to_email}' — {str(e)}\n"
        print(error_message)
        with open("log.txt", "a") as log:
            log.write(error_message)
