import requests

API_KEY = "YOUR_API_KEY"   # Replace with your OpenWeather API key

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n------ Weather Report ------")
    print("City:", data["name"])
    print("Country:", data["sys"]["country"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")
    print("Weather:", data["weather"][0]["description"].title())
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("City not found or invalid API key.")