from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask CI/CD</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: white;
                width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }

            h1 {
                color: #333;
            }

            .success {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 Flask CI/CD Demo</h1>

            <p>Ship code with confidence.</p>
            <p>CI/CD Lab</p>

            <p>
                This website is deployed using
                Continuous Integration and Continuous Deployment.
            </p>

            <p class="success">
                ✓ Application is running
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/pipeline")
def pipeline():
    return """
    <html>
    <head><title>Pipeline</title></head>
    <body>
        <h1>CI/CD Pipeline</h1>
        <p>From commit to deployment</p>
    </body>
    </html>
    """


@app.route("/about")
def about():
    return """
    <html>
    <head><title>About</title></head>
    <body>
        <h1>Why this demo exists</h1>
        <p>This project demonstrates a basic Flask CI/CD workflow.</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy", "service": "ci-cd-example"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
