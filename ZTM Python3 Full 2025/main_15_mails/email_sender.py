from pathlib import Path
from string import Template
from email.message import EmailMessage
import smtplib
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_SENDER_PASSWORD = os.getenv(
    "EMAIL_SENDER_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
SENDER_NAME = os.getenv("NAME_SENDER")
SUBJECT = "Yeeey, Python go go go blue world!"

if not EMAIL_SENDER or not EMAIL_SENDER_PASSWORD or not EMAIL_RECEIVER or not SENDER_NAME:
    raise ValueError("Please set EMAIL_SENDER, EMAIL_SENDER_PASSWORD, EMAIL_RECEIVER, and NAME_SENDER in your .env file.")

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "email_template.html"

if not TEMPLATE_PATH.is_file():
    raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")

html_tpl = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
html = html_tpl.substitute({"name": "Python Master"})

email = EmailMessage()
email["From"] = f"{SENDER_NAME} <{EMAIL_SENDER}>"
email["To"] = EMAIL_RECEIVER
email["Subject"] = SUBJECT

email.set_content("Your email client does not support HTML.")
email.add_alternative(html, subtype="html")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

try:
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_SENDER_PASSWORD)
        smtp.send_message(email)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print("Auth error.")
    raise
except Exception as e:
    print("Failed to send email:", repr(e))
    raise
