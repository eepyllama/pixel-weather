from flask import Flask
from dotenv import load_dotenv
from routes.weather_routes import weather_bp

# Load the .env file so os.environ can see our secrets
load_dotenv

app = Flask(__name__) #create my website under variable name "app"

# Register our blueprint — all its routes are now active
app.register_blueprint(weather_bp)

if __name__== '__main__':
  app.run(debug=True) # used in developing for error handling, not in production

