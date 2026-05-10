from flask import Blueprint, render_template, request
from services.weather_service import get_weather

# A blueprint is Flask's way of organizing routes into groups.
# Think of it as a mini Flask app that gets registered
# onto the main app later. The first argument is the name, 
# the second tells the Flask where to find the templates/static files.

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/')
def home():
  return render_template('index.html', weather= None, error= None)

@weather_bp.route('/weather', methods=['POST'])
def weather():
  city= request.form.get('city','').strip()

  # .strip() removes accidental whitespace
  # " Tokyo " becomes "Tokyo"

  if not city:
    return render_template(
      'index.html',
      weather= None,
      error= "Please enter a city name."
    )
  
  #Unpack the tuple our service returns
  weather_data, error = get_weather(city)

  return render_template(
    'index.html',
    weather=weather_data,
    error=error
  )