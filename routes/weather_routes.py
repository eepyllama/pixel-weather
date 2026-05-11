from flask import Blueprint, render_template, request
from services.weather_service import get_weather, get_forecast

# A blueprint is Flask's way of organizing routes into groups.
# Think of it as a mini Flask app that gets registered
# onto the main app later. The first argument is the name, 
# the second tells the Flask where to find the templates/static files.

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/')
def home():
  return render_template('index.html', weather= None, forecast=None, error= None)

@weather_bp.route('/weather', methods=['POST'])
def weather():
  city= request.form.get('city','').strip()

  # .strip() removes accidental whitespace
  # " Tokyo " becomes "Tokyo"

  if not city:
    return render_template(
      'index.html',
      weather= None,
      forecast= None,
      error= "PLEASE ENTER A CITY NAME."
    )
  
  # Fetch both simultaneously — current weather AND forecast
  weather_data, weather_error = get_weather(city)
  forecast_data, forecast_error = get_forecast(city)

  #Current weather error is the priority error to show
  error = weather_error or forecast_error

  return render_template(
    'index.html',
    weather=weather_data,
    forecast=forecast_data,
    error=error
  )