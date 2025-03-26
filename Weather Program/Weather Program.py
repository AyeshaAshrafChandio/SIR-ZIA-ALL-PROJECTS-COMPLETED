import requests

def get_weather():
    print("=== Simple Weather App ===")
    
    # Get user input
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    
    # API request
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return
        
        # Display weather info
        print(f"\nWeather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Conditions: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} km/h")
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    get_weather()