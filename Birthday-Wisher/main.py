import smtplib
import datetime as dt
import random

MY_EMAIL = "INSERT YOUR EMAIL"
PASSWORD = "INSERT YOUR PASSWORD"
OTHER_EMAIL = "INSERT EMAIL YOU WISH TO SEND A MESSAGE"


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open (r"/Birthday_Wisher_start/quotes.txt") as quotes:
        list_of_quotes = quotes.readlines()
        random_quote = random.choice(list_of_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=OTHER_EMAIL, 
        msg=f"Subject: Motivacional\n\n{random_quote}")
    connection.close()

