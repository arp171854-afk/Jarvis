import requests

def get_weather(city="Ahmedabad", api_key="42595f9f646e5fe60427ae2c48724eee"):
    """
    Fetches current weather for a given city using OpenWeather API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        data = requests.get(url, timeout=8).json()
        if data.get("main"):
            temp = round(data["main"]["temp"])
            desc = data["weather"][0]["description"]
            return f"Temperature in {city} is {temp}°C with {desc}."
        else:
            return "I couldn't fetch the weather right now."
    except:
        return "Weather service is not responding."
