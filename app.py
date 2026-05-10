from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load the .env file so os.environ can see our secrets
load_dotenv

app = Flask(__name__) #create my website under variable name "app"

def get_weather_data(city):
  '''
  A dedicated function just for talking to the OpenWeather API.
  Keeping API logic separate from route logic is a professional habit.
  It makes your code easier to test and easier to change later. 
  '''
  api_key = os.environ.get('OPENWEATHER_API_KEY')

  # Build the URL with parameters
  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {
    'q' : city,
    'appid': api_key,
    'units':'metric'
  }

  # Make the HTTP GET request to OpenWeather
  response= requests.get(url, params= params)

  #.json() converts the JSON text into python dictionary
  data = response.json()
  return data

@app.route('/') #when someone sends a GET request to root URL  run the following code 
def home():
  return render_template('index.html', weather = None, error= None)

# @app.route('/about')
# def about():
#   return 'This is a cutesy weather app :3 '

@app.route('/weather', methods= ['POST'])
def weather():
  city = request.form.get('city')

  #call our dedicated function
  data = get_weather_data(city)

  #check if OpenWeather returned an error 
  #OpenWeather uses "cod" (code) field: 200 = success, 404 = city not found
  if data.get('cod') != 200:
    return render_template('index.html', weather= None, error = "City not found")
  
  #Extract only what we need from the JSON
  weather= {
    'city' : data['name'],
    'country': data['sys']['country'],
    'temperature': round(data['main']['temp']),
    'feels_like': round(data['main']['humidity']),
    'humidity': data['main']['humidity'],
    'description': data['weather'][0]['description'].title(),
    'icon':data['weather'][0]['icon']
  }

  return render_template('index.html', weather = weather)

if __name__== '__main__':
  app.run(debug=True) # used in developing for error handling, not in production

