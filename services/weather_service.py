import requests
import os
from collections import Counter
from datetime import datetime

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

def get_forecast(city):
    """
    Fetches a 5-day forecast collapsed into daily summaries.
    
    The /forecast endpoint returns 40 entries (every 3 hrs).
    We group by date, then extract max/min temp and the
    most common weather description per day.
    
    Returns: (forecast_list, error_string)
    """
    api_key = os.environ.get('OPENWEATHER_API_KEY')

    if not api_key:
        return None, "API key missing."

    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if data.get('cod') != '200':
            return None, data.get('message', 'Forecast unavailable.').capitalize()

        # 'list' is the key OpenWeather uses for the 40 snapshots
        # Each item has 'dt_txt': "2024-05-12 15:00:00"
        snapshots = data['list']

        # Group snapshots by date using a dictionary
        # Keys will be date strings like "2024-05-12"
        # Values will be lists of snapshots for that date
        days = {}
        for snap in snapshots:
            # Split "2024-05-12 15:00:00" → take just "2024-05-12"
            date_str = snap['dt_txt'].split(' ')[0]

            if date_str not in days:
                days[date_str] = []

            days[date_str].append(snap)

        # Now collapse each day into one summary
        forecast = []

        # Skip today (index 0) — user already sees current weather
        # Take the next 5 days
        for date_str in list(days.keys())[1:6]:
            day_snaps = days[date_str]

            # Max and min temp across all snapshots that day
            temps = [s['main']['temp'] for s in day_snaps]
            max_temp = round(max(temps))
            min_temp = round(min(temps))

            # Most common description — Counter counts occurrences
            # most_common(1) returns [(description, count)]
            # [0][0] gets just the description string
            descriptions = [s['weather'][0]['description'] for s in day_snaps]
            description = Counter(descriptions).most_common(1)[0][0].title()

            # Most common icon code for that day
            icons = [s['weather'][0]['icon'] for s in day_snaps]
            icon = Counter(icons).most_common(1)[0][0]

            # Convert "2024-05-12" to "MON", "TUE" etc.
            # strptime parses a string into a datetime object
            # strftime formats a datetime object into a string
            # "%A" = full weekday name, [:3] takes first 3 letters
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            day_name = date_obj.strftime('%A')[:3].upper()

            forecast.append({
                'day':         day_name,
                'date':        date_str,
                'max_temp':    max_temp,
                'min_temp':    min_temp,
                'description': description,
                'icon':        icon,
            })

        return forecast, None

    except requests.exceptions.ConnectionError:
        return None, "Can't reach the forecast service."
    except requests.exceptions.Timeout:
        return None, "Forecast service timed out."
    except Exception as e:
        return None, f"Forecast error: {str(e)}"


