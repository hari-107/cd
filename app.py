from flask import Flask, request
import os
import requests

app = Flask(__name__)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>kanguva Dashboard</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    min-height: 100vh;
    font-family: Inter, Arial, sans-serif;
    color: #fff;
    background: linear-gradient(135deg, #0f172a, #164e63 55%, #0e7490);
}
.container { width: min(1100px, 92%); margin: auto; padding: 32px 0 50px; }
header { display:flex; justify-content:space-between; align-items:center; gap:20px; margin-bottom:28px; }
.brand { font-size: 25px; font-weight: 800; }
.brand span { opacity:.7; font-weight:500; font-size:14px; display:block; margin-top:4px; }
.search { display:flex; gap:10px; width:min(520px,100%); }
.search input { flex:1; min-width:0; padding:14px 18px; border:0; border-radius:14px; outline:none; font-size:16px; }
.search button { padding:14px 22px; border:0; border-radius:14px; background:#fff; color:#0f172a; font-weight:700; cursor:pointer; }
.hero { padding:32px; border:1px solid rgba(255,255,255,.16); border-radius:28px; background:rgba(255,255,255,.10); backdrop-filter:blur(14px); }
.location { font-size:18px; opacity:.8; }
.main-weather { display:flex; justify-content:space-between; align-items:center; gap:30px; margin-top:20px; }
.temp { font-size:76px; line-height:1; font-weight:800; }
.condition { font-size:22px; text-transform:capitalize; margin-top:10px; opacity:.9; }
.weather-icon { font-size:90px; }
.grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:18px; }
.card { padding:22px; border-radius:20px; background:rgba(255,255,255,.10); border:1px solid rgba(255,255,255,.12); }
.label { font-size:13px; opacity:.65; margin-bottom:10px; }
.value { font-size:25px; font-weight:750; }
.status { margin-top:20px; min-height:24px; opacity:.75; text-align:center; }
@media(max-width:800px) { header { flex-direction:column; align-items:stretch; } .main-weather { flex-direction:column; align-items:flex-start; } .grid { grid-template-columns:repeat(2,1fr); } }
@media(max-width:480px) { .search { flex-direction:column; } .grid { grid-template-columns:1fr; } .temp { font-size:60px; } .hero { padding:24px; } }
</style>
</head>
<body>
<div class="container">
<header>
    <div class="brand">🌤️ Weather Dashboard<span>Live conditions powered by OpenWeather</span></div>
    <form class="search" id="searchForm">
        <input id="cityInput" value="Coimbatore" placeholder="Search city..." autocomplete="off">
        <button type="submit">Search</button>
    </form>
</header>

<section class="hero">
    <div class="location" id="location">Loading weather...</div>
    <div class="main-weather">
        <div>
            <div class="temp" id="temperature">--°C</div>
            <div class="condition" id="condition">Fetching current conditions</div>
        </div>
        <div class="weather-icon" id="icon">🌤️</div>
    </div>
</section>

<div class="grid">
    <div class="card"><div class="label">Feels Like</div><div class="value" id="feels">--°C</div></div>
    <div class="card"><div class="label">Humidity</div><div class="value" id="humidity">--%</div></div>
    <div class="card"><div class="label">Wind</div><div class="value" id="wind">-- m/s</div></div>
    <div class="card"><div class="label">Pressure</div><div class="value" id="pressure">-- hPa</div></div>
    <div class="card"><div class="label">Visibility</div><div class="value" id="visibility">-- km</div></div>
    <div class="card"><div class="label">Cloudiness</div><div class="value" id="clouds">--%</div></div>
    <div class="card"><div class="label">Min Temperature</div><div class="value" id="minTemp">--°C</div></div>
    <div class="card"><div class="label">Max Temperature</div><div class="value" id="maxTemp">--°C</div></div>
</div>
<div class="status" id="status" aria-live="polite"></div>
</div>
<script>
const $ = id => document.getElementById(id);
const iconMap = {
    Clear: '☀️', Clouds: '☁️', Rain: '🌧️', Drizzle: '🌦️', Thunderstorm: '⛈️',
    Snow: '❄️', Mist: '🌫️', Smoke: '🌫️', Haze: '🌫️', Dust: '🌫️', Fog: '🌫️'
};

async function loadWeather(city) {
    $('status').textContent = 'Updating weather...';
    try {
        const response = await fetch('/weather?city=' + encodeURIComponent(city));
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'Unable to fetch weather');

        $('location').textContent = `${data.city}, ${data.country}`;
        $('temperature').textContent = `${Math.round(data.temperature)}°C`;
        $('condition').textContent = data.weather;
        $('icon').textContent = iconMap[data.weather_main] || '🌤️';
        $('feels').textContent = `${Math.round(data.feels_like)}°C`;
        $('humidity').textContent = `${data.humidity}%`;
        $('wind').textContent = `${data.wind_speed} m/s`;
        $('pressure').textContent = `${data.pressure} hPa`;
        $('visibility').textContent = `${data.visibility} km`;
        $('clouds').textContent = `${data.clouds}%`;
        $('minTemp').textContent = `${Math.round(data.temp_min)}°C`;
        $('maxTemp').textContent = `${Math.round(data.temp_max)}°C`;
        $('status').textContent = `Last updated: ${new Date().toLocaleTimeString()}`;
    } catch (error) {
        $('status').textContent = error.message;
    }
}

$('searchForm').addEventListener('submit', event => {
    event.preventDefault();
    const city = $('cityInput').value.trim();
    if (city) loadWeather(city);
});

loadWeather('Coimbatore');
</script>
</body>
</html>
"""


@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()
    if not city:
        return {"error": "City is required"}, 400
    if not WEATHER_API_KEY:
        return {"error": "Weather API key is not configured", "city": city}, 500

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"},
            timeout=10,
        )
        data = response.json()
        if response.status_code != 200:
            return {"error": data.get("message", "Unable to fetch weather")}, response.status_code

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "visibility": round(data.get("visibility", 0) / 1000, 1),
            "clouds": data.get("clouds", {}).get("all", 0),
            "weather": data["weather"][0]["description"],
            "weather_main": data["weather"][0]["main"],
        }
    except requests.RequestException:
        return {"error": "Weather service is unavailable"}, 503


@app.route("/health")
def health():
    return {"status": "healthy", "service": "weather-app"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
