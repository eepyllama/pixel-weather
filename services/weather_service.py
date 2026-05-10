import requests
import os

def get_weather(city):
  """
  Fetches current weather data for a given city.

  Returns a tuple: (weather_dict, error_string)
  On success: (weather_dict, None)
  On Failure: (None, error_message)

  Returning a tuple of (data, error) is a clean pattern -
  the caller always knows exactly what they're getting.
  """
  api_key = os.environ.get('OPENWEATHER_API_KEY')

  if not api_key:
    return None, "API key missing. Check your .env file."
  
  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {
    'q' : city,
    'appid': api_key,
    'units':'metric'
  }

  try:
    response = requests.get (url, params=params, timeout=5)
    data = response.json()
    # OpenWeather returns cod=200 for success
    # It returns cod="404" (as a string!) for city not found
    # Note: always use != 200, not == 404, to catch all error types
    if data.get('cod') != 200:
        message = data.get('message', 'City not found.')
        return None, message.capitalize()
    
    # Extract and clean the data we care about
    weather = {
        'city':        data['name'],
        'country':     data['sys']['country'],
        'temperature': round(data['main']['temp']),
        'feels_like':  round(data['main']['feels_like']),
        'humidity':    data['main']['humidity'],
        'description': data['weather'][0]['description'].title(),
        'icon':        data['weather'][0]['icon'],
        'wind_speed':  data['wind']['speed'],
    }
    
    return weather, None
  
  except requests.exceptions.ConnectionError:
     return None, "Can't reach the weather service. Check your internet connection."
  
  except requests.exceptions.Timeout:
     return None, "The weather service took too long to respond. Try again."
  
  except Exception as e:
     #catch-all for unexpected erros
     #In development, we want to see the real error
     return None, f"Something went wrong: {str(e)}"