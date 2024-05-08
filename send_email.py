import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(message):
    host = os.getenv("HOST")
    port = 465

    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("EMAIL_RECEIVER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
