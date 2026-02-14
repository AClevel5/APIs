import requests
from datetime import datetime

MY_LAT = 39.6136
MY_LONG = -105.0165







def is_iss_overhead(MY_LAT, MY_LONG):
    parameters = {"lat": MY_LAT,
                  "lng": MY_LONG,
                  "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour

    if (sunset + 24) > current_hour > sunrise:
        # iss
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        # Raise Exceptions for Errors
        iss_response.raise_for_status()
        longitude = float(iss_response.json()["iss_position"]["longitude"])
        latitude = float(iss_response.json()["iss_position"]["latitude"])
        iss_position = (longitude, latitude)



