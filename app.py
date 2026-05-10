from flask import Flask, render_template, request
app = Flask(__name__) #create my website under variable name "app"

@app.route('/') #when someone sends a GET request to root URL  run the following code 
def home():
  return render_template('index.html', weather = None)

# @app.route('/about')
# def about():
#   return 'This is a cutesy weather app :3 '

@app.route('/weather', methods= ['POST'])
def get_weather():
  city = request.form.get('city')

  weather= {
    'city' : city,
    'temperature': 24,
    'description': 'Sunny skies ahead!'
  }

  return render_template('index.html', weather = weather)

if __name__== '__main__':
  app.run(debug=True) # used in developing for error handling, not in production

