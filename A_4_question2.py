import requests

def weather(city):
    api_key = "51b9ac4fb517678e23fe926abeb4a327"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        visibility = data.get("visibility", "N/A")
        sea_level_pressure = data["main"].get("sea_level", "N/A")
        ground_level_pressure = data["main"].get("grnd_level", "N/A")
        rain = data.get("rain", {}).get("1h", 0)  # Use .get() to avoid KeyError

        print(f"Weather in: {city}")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Visibility in the city: {visibility}")
        print(f"Sea level pressure: {sea_level_pressure}")
        print(f"Ground level pressure: {ground_level_pressure}")
        print(f"Rain (last 1h): {rain} mm")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the weather data: {e}")
    except KeyError:
        print("Error: Unable to parse weather data (maybe wrong city name)")

city = input("Enter the name of the city: ")
weather(city)
