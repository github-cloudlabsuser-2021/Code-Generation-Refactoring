import requests

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        """
        Get weather data for a specified city.

        Parameters:
        city (str): The name of the city to get the weather for.

        Returns:
        dict: A dictionary containing weather data for the specified city.
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

if __name__ == "__main__":
    api_key = "2aaace6356ac41f7d87d742367fe19b3"  # Replace with your OpenWeatherMap API key
    weather = Weather(api_key)
    
    city = input("Enter the city name: ")
    data = weather.get_weather(city)
    
    if data:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or API request failed.")