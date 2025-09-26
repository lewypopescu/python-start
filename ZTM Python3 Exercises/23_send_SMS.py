from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
messaging_sid = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
to_number = os.getenv("PHONE_NUMBER_RECEIVER")

client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        messaging_service_sid=messaging_sid,
        body="Python is awesome! Sent with Twilio and Python. Lewyyy💙",
        to=to_number
    )
    print(f"Message SID: {message.sid}")
    print(f"Status: {message.status}")
except Exception as e:
    print(f"Error: {e}")


# Twilio is a cloud communications platform that allows you to send and receive messages, make and receive phone calls, and perform other communication functions using its APIs. It is commonly used for building applications that require SMS, voice, and messaging capabilities.
# Remember to keep your authentication credentials secure and avoid hardcoding them directly in your code. Using environment variables, as shown in the example, is a good practice for managing sensitive information.
# Always refer to the latest Twilio documentation for any updates or changes in their API and usage guidelines.

# Good luck, Lewy! You are awesome! ;) # I believe in you! ;)
