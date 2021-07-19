from decimal import Decimal
from re import sub
import requests
from bs4 import BeautifulSoup
from smtplib import *

STANDARD_PRICE = 1500.00
URL = "https://www.amazon.in/Dell-Km117-Wireless-Keyboard-Mouse/dp/B01LOORNLY/ref=psdc_1375418031_t1_B084GQV1YP"
HEADER = {
        "Accept-Language" : "en-US,en;q=0.9,hi;q=0.8",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

FROM_ADDRESS = "testingmain19@gmail.com"
PASSWORD = "Qwerty@12345"
TARGET_ADDRESS = "muditshukla010@gmail.com"

def get_price():
    response = requests.get(url= URL, headers=HEADER)
    soup = BeautifulSoup(response.text, "lxml")
    price= soup.find(id="priceblock_ourprice").text[1::]
    price = Decimal(sub(r'[^\d.]', '', price))
    return price


def send_mail_alert(price):
    connection = SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=FROM_ADDRESS, password=PASSWORD)
    connection.sendmail(from_addr=FROM_ADDRESS, to_addrs=TARGET_ADDRESS,
                        msg="Subject: Price drop alert \n\n "
                            "The price of the selected commodity has dropped below the standard level set by you \n\n"
                            "The link to the respective item is \n\n"
                            f"{URL}")
    connection.close()

actual_price = get_price()
if STANDARD_PRICE > actual_price:
    send_mail_alert(actual_price)



