import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -27.469770
MY_LONG = 153.025131

MY_EMAIL = "pythontest6568@gmail.com"
PASSWORD = "lima101010"

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():

    paramaters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=paramaters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour() 
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="celisgabriel97@gmail.com",
            msg="Subject:Olha pra cima👆\n\nA estação espacial internacional está passando por cima de você agora maninho!"
        )