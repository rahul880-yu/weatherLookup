import requests


def get_weather(api_key, city_name, country_code="IN"):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city_name},{country_code}",
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        city = data["name"]
        country = data["sys"]["country"]
        print(f"Weather in {city}, {country}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    else:
        print(
            f"Error fetching weather data. Status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    city_name = "Mumbai"  # Replace with the city in India you want to check the weather for
    get_weather(api_key, city_name)
