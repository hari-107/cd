from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Weather Application" in response.data
    assert b"Check the current weather for any city." in response.data


def test_weather_missing_city():
    client = app.test_client()

    response = client.get("/weather")

    assert response.status_code == 400
    assert response.json["error"] == "City is required"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["service"] == "weather-app"
