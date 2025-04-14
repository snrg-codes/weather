import requests
from typing import Dict, Optional
from datetime import datetime


def get_weather(city: str, api_key: str) -> Dict:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Use metric units (Celsius)
        }
        
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        
        if data['cod'] != 200:
            raise ValueError(f"Error: {data['message']}")
            
        # Extract relevant weather information
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'country': data['sys']['country'],
            'icon': data['weather'][0]['icon'],
            'pressure': data['main']['pressure'],
            'visibility': data.get('visibility', 'N/A'),
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset']
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error fetching weather data: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Error parsing weather data: {str(e)}")
