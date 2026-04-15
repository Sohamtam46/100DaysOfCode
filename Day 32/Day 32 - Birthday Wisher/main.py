##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import random
import datetime as dt
import pandas as pd
birthday_today = False

NAME_PLACEHOLDER = "[NAME]"
AGE_PLACEHOLDER = "[AGE]"

# getting current day details
now = dt.datetime.now()
present_year = now.year
present_day = now.day
present_month = now.month
# getting the birthday details
birthdays = pd.read_csv("birthdays.csv")

birthdays_dict = birthdays.to_dict(orient="records")
for people_details in birthdays_dict:
    if people_details["month"] == present_month and people_details["day"] == present_day:
        birthday_person_details = people_details
        birthday_today = True

MY_EMAIL = "test@gmail.com"
PASSWORD = "test"

if birthday_today:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as data:
        letter = data.read()
        output_letter_rough =letter.replace(NAME_PLACEHOLDER,birthday_person_details["name"])
        age = present_year - birthday_person_details["year"]
        output_letter = output_letter_rough.replace(AGE_PLACEHOLDER,str(age))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=birthday_person_details["email"],
                            msg=f"Subject:Birthday Wishes!\n\n{output_letter}"
                            )


