# ⛅ PIXEL WEATHER
### FORECAST SYSTEM v1.0

> *A cozy pixel art weather app built with Python, Flask, and the OpenWeather API.*
> *Check real-time weather and 5-day forecasts for any city on Earth — rendered in full retro glory.*

---

## 🌐 Live Demo

**[https://pixel-weather-u2c5.onrender.com](https://pixel-weather-u2c5.onrender.com)**

> ⚠️ Hosted on Render's free tier — the server spins down after inactivity.
> First load may take 30–60 seconds to wake up. Worth the wait. 🎮

---

## 📸 Preview

<!-- 
  SUGGESTION: Replace this section with actual screenshots once you take them.
  Ideal shots to capture:
    1. Homepage (before search) — shows the pixel background + search bar
    2. A sunny city result — golden background mood
    3. A rainy city result — deep ocean blue mood
    4. The 5-day forecast grid visible below the card
    5. Mobile view (open DevTools → toggle device toolbar → screenshot)

  To add images:
    - Create a folder in your repo: /assets/screenshots/
    - Upload your screenshots there via GitHub or git
    - Replace the placeholder links below with the real paths

  Example once done:
    ![Homepage](assets/screenshots/homepage.png)
    ![Rainy Mood](assets/screenshots/rainy.png)
-->

| Homepage | Weather Card | Forecast |
|----------|-------------|----------|
| `📷 screenshot coming soon` | `📷 screenshot coming soon` | `📷 screenshot coming soon` |

---

## ✨ Features

- 🌤️ **Real-time weather** — current temperature, description, humidity, wind speed, feels like
- 📅 **5-day forecast** — daily high/low temps with dominant weather condition per day
- 🎨 **Dynamic pixel art backgrounds** — the entire scene changes based on weather mood
- 🖥️ **Retro pixel UI** — Press Start 2P font, RPG-style stat panel, gold pixel card borders
- ⌨️ **Typewriter mood messages** — flavour text that matches the weather condition
- ⚡ **Glitch animation** — on invalid city searches
- 📱 **Responsive design** — works on mobile and desktop
- 🌙 **Day/Night awareness** — separate moods for daytime and night conditions

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Templating | Jinja2 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| API | [OpenWeather API](https://openweathermap.org/api) (Current + Forecast) |
| Font | [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) — Google Fonts |
| Deployment | [Render.com](https://render.com) |
| Version Control | Git + GitHub |

---

## 🏗️ Project Architecture

```
pixel-weather/
├── routes/
│   ├── __init__.py
│   └── weather_routes.py       # URL routing — connects URLs to functions
├── services/
│   ├── __init__.py
│   └── weather_service.py      # All API logic — current weather + forecast
├── static/
│   ├── css/
│   │   └── style.css           # Full pixel art design system
│   ├── js/
│   │   └── main.js             # Mood engine + typewriter + forecast icons
│   └── images/
│       └── bg-*.png            # Pixel art background images per mood
├── templates/
│   └── index.html              # Jinja2 template — structure + data binding
├── venv/                       # Virtual environment (not committed)
├── .env                        # Secret API key (not committed)
├── .gitignore
├── app.py                      # Entry point — creates Flask app
├── render.yaml                 # Render deployment config
└── requirements.txt            # Python dependencies
```

**Separation of concerns:** every file has exactly one job.
Routes call services. Services call APIs. Templates display data. `app.py` assembles everything.

---

## 🚀 Run Locally

### Prerequisites
- Python 3.8+
- A free [OpenWeather API key](https://openweathermap.org/appid)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/eepyllama/pixel-weather.git
cd pixel-weather

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env file
echo OPENWEATHER_API_KEY=your_key_here > .env

# 5. Run the development server
python app.py
```

Then open **http://localhost:5000** in your browser.

---

## 🌦️ Weather Mood System

The app maps OpenWeather icon codes to visual moods that change the entire background scene:

| Mood | Conditions | Background |
|------|-----------|------------|
| ☀️ Sunny | Clear sky (day) | Warm golden gradient |
| ⛅ Cloudy | Partly/mostly cloudy | Steel blue-grey |
| 🌧️ Rainy | Drizzle, rain | Deep ocean teal |
| ⛈️ Stormy | Thunderstorm | Dark dramatic purple |
| ❄️ Snow | Snow | Crisp ice blue |
| 🌫️ Mist | Fog, haze, mist | Soft grey |
| 🌙 Night | Any night condition | Midnight deep |

Each mood also triggers a unique typewriter message in the card footer.

---

## 📖 What I Learned Building This

This project was built as a **mentorship-style learning journey** covering:

- **Flask fundamentals** — routing, Blueprints, `render_template`, `request.form`
- **REST APIs** — HTTP methods, JSON parsing, query parameters, error handling
- **Jinja2 templating** — template inheritance, filters, conditional rendering
- **Professional project structure** — separation of concerns, modular architecture
- **CSS design systems** — custom properties, pixel art aesthetics, animations, `backdrop-filter`
- **JavaScript DOM manipulation** — data attributes, typewriter effects, cancellation tokens
- **Environment variables** — keeping secrets out of code with `.env` and `python-dotenv`
- **Git workflow** — incremental commits, `.gitignore`, pushing to GitHub
- **Production deployment** — Gunicorn, Render.com, CI/CD via GitHub integration

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENWEATHER_API_KEY` | Your OpenWeather API key — get one free at [openweathermap.org](https://openweathermap.org/appid) |

Never commit your `.env` file. It's already in `.gitignore`.

---

## 🗺️ Roadmap

Things I plan to add next:

- [ ] Hourly temperature chart using Chart.js
- [ ] Loading spinner during API fetch
- [ ] Cache repeated city searches with Flask-Caching
- [ ] Custom pixel art backgrounds for each weather mood
- [ ] Search history stored in session
- [ ] Unit toggle (°C / °F)

---

## 🙏 Acknowledgements

- Weather data by [OpenWeather API](https://openweathermap.org)
- Pixel font [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) by CodeMan38
- Pixel art background inspiration from [itch.io](https://itch.io/game-assets/free/tag-pixel-art)
- Built with guidance from [Anthropic Claude](https://claude.ai) — mentorship-style

---

## 📄 License

MIT License — feel free to fork, modify, and build on this project.

---

<p align="center">
  Built with 🎮 and way too much caffeine
  <br><br>
  <a href="https://pixel-weather-u2c5.onrender.com">🌐 Live Site</a> ·
  <a href="https://github.com/eepyllama/pixel-weather/issues">🐛 Report Bug</a> ·
  <a href="https://github.com/eepyllama/pixel-weather/issues">✨ Request Feature</a>
</p>
