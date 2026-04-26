import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(account_sid, auth_token)

    def format_message(self,message_data):
        return (f"Low price alert! Only EUR {message_data[0]} to fly from DUB to {message_data[1]}, "
                f"on {message_data[2]} until {message_data[3]} with {message_data[4]} layover(s).")

    def send_message(self,message_data):
        message = self.format_message(message_data)
        message = self.client.messages.create(
            from_=f"whatsapp:{os.getenv("FROM_NUMBER")}",
            body=f"{message}",
            to=f'whatsapp:{os.getenv("TO_NUMBER")}'
        )
        print("message sent")

    def send_email(self,user_email,message_data):
        message = self.format_message(message_data)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
            connection.sendmail(
                from_addr=os.getenv("MY_EMAIL"),
                to_addrs=user_email,
                msg=f"Subject:A Cheaper Flight Deal Found!\n\n{message}"
            )
        print("Email Sent")
