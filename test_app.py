from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Ship code with confidence." in response.data
    assert b"CI/CD Lab" in response.data


def test_pipeline():
    client = app.test_client()

    response = client.get("/pipeline")

    assert response.status_code == 200
    assert b"From commit to deployment" in response.data


def test_about():
    client = app.test_client()

    response = client.get("/about")

    assert response.status_code == 200
    assert b"Why this demo exists" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["service"] == "ci-cd-example"
