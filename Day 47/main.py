import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

TARGET_PRICE = 120.00
URL = "https://www.amazon.ie/Amazfit-Control-Material-Waterproof-Silicone/dp/B0DSPWKJW4/ref=sr_1_2?sr=8-2"
HEADER = {"User-Agent":"CCBot/2.0 (https://commoncrawl.org/faq/)","Accept-Language":"en-US,en;q=0.5"}

# --- Fetching Amazon Product Site HTML
response = requests.get(url=URL)
amazon_product_page = response.text

soup = BeautifulSoup(amazon_product_page, "lxml")

product_title = soup.find(id="productTitle")
product_price = soup.find(class_="a-price-whole")
product_price_decimal = soup.find(class_="a-price-fraction")

product_price_whole = float(product_price.text + product_price_decimal.text)



def send_email():
    message = (f"The Product: {product_title.text.strip()} is now below your target price and is for EUR {product_price_whole}! \n"
               f"Go Grab it at {URL}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("MY_EMAIL"),
            to_addrs="Test",
            msg=f"Subject:A better deal on Amazon Found!\n\n{message}"
        )

if product_price_whole < TARGET_PRICE:
    send_email()