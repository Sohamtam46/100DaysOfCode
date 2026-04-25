import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(account_sid, auth_token)

    def format_message(self,message_data):
        return (f"Low price alert! Only €{message_data[0]} to fly from DUB to {message_data[1]}, "
                f"on {message_data[2]} until {message_data[3]}")

    def send_message(self,message_data):
        message = self.format_message(message_data)
        message = self.client.messages.create(
            from_=f"whatsapp:{os.getenv("FROM_NUMBER")}",
            body=f"{message}",
            to=f'whatsapp:{os.getenv("TO_NUMBER")}'
        )
        print("message sent")
