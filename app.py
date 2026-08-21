from flask import Flask, request
import requests
import os

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #74ebd5, #ACB6E5);
                text-align: center;
                padding-top: 80px;
            }
            .container {
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            }
            h1 { color: #333; }
            input, button {
                padding: 12px;
                margin: 8px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
            button {
                background: #333;
                color: white;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌤️ Weather Application</h1>
            <p>Check the current weather for any city.</p>
            <form action="/weather" method="get">
                <input name="city" placeholder="Enter city" required>
                <button type="submit">Get Weather</button>
            </form>
        </div>
    </body>
    </html>
    """


@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()

    if not city:
        return {"error": "City is required"}, 400

    if not WEATHER_API_KEY:
        return {
            "error": "Weather API key is not configured",
            "city": city
        }, 500

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get("message", "Unable to fetch weather")
            }, response.status_code

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }

    except requests.RequestException:
        return {"error": "Weather service is unavailable"}, 503


@app.route("/health")
def health():
    return {"status": "healthy", "service": "weather-app"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
