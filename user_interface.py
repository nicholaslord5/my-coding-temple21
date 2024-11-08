# user_interface.py

from weather_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.parser = parser

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch(city)
        return self.parser.parse(data)

    def display_weather(self, city):
        data = self.fetcher.fetch(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse(data)
            print(weather_report)

    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                self.display_weather(city)
                forecast = None
            if forecast:
                print(forecast)