from flask import Flask

app = Flask(__name__)

STYLE = """
<style>
*{box-sizing:border-box}body{margin:0;font-family:Inter,Arial,sans-serif;background:#0b1020;color:#e8ecf7}nav{display:flex;justify-content:space-between;align-items:center;padding:20px 8%;background:#111936;border-bottom:1px solid #26304f;position:sticky;top:0}.brand{font-weight:800;font-size:20px}.links a{color:#aeb8d4;text-decoration:none;margin-left:24px}.links a:hover{color:#fff}.hero,.page{max-width:1050px;margin:auto;padding:80px 8%}.hero{text-align:center}.badge{display:inline-block;padding:7px 12px;border:1px solid #33406a;border-radius:999px;color:#8fd3ff;font-size:13px}.hero h1{font-size:52px;margin:20px 0 12px}.hero p,.page>p{color:#aeb8d4;line-height:1.7}.btn{display:inline-block;margin-top:18px;padding:12px 20px;border-radius:10px;background:#4f7cff;color:white;text-decoration:none;font-weight:700}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:35px}.card{background:#111936;border:1px solid #26304f;border-radius:16px;padding:24px}.card h3{margin-top:0}.ok{color:#5ee39a}.muted{color:#8994b3}.steps{counter-reset:item}.step{margin:16px 0;padding:18px;border-left:3px solid #4f7cff;background:#111936;border-radius:0 12px 12px 0}.code{font-family:monospace;background:#080c18;padding:18px;border-radius:12px;overflow:auto;color:#b9c7ff}footer{text-align:center;padding:35px;color:#687391;border-top:1px solid #202946}@media(max-width:700px){.hero h1{font-size:38px}.grid{grid-template-columns:1fr}.links a{margin-left:10px}}
</style>
"""


def layout(title, content):
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | CI/CD Demo</title>{STYLE}</head><body><nav><div class="brand">⚡ CI/CD Lab</div><div class="links"><a href="/">Home</a><a href="/pipeline">Pipeline</a><a href="/about">About</a><a href="/health">Health</a></div></nav>{content}<footer>Flask • Docker • Jenkins • Automated Testing</footer></body></html>'''


@app.route("/")
def home():
    return layout("Home", '''<main class="hero"><span class="badge">CONTINUOUS DELIVERY DEMO</span><h1>Ship code with confidence.</h1><p>A small Flask application demonstrating how source control, automated tests, Docker and Jenkins fit together in a CI/CD workflow.</p><a class="btn" href="/pipeline">Explore the pipeline →</a><div class="grid"><div class="card"><h3>🔄 Continuous Integration</h3><p class="muted">Every change can trigger an automated build and test cycle.</p></div><div class="card"><h3>🐳 Containerized</h3><p class="muted">The app is packaged consistently with Docker.</p></div><div class="card"><h3>🚀 Continuous Delivery</h3><p class="muted">A successful pipeline leaves a repeatable deployment artifact.</p></div></div></main>''')


@app.route("/pipeline")
def pipeline():
    return layout("Pipeline", '''<main class="page"><span class="badge">PIPELINE</span><h1>From commit to deployment</h1><p>The project uses a simple, easy-to-understand delivery flow.</p><div class="steps"><div class="step"><b>01 · Commit</b><br><span class="muted">Push application changes to GitHub.</span></div><div class="step"><b>02 · Build</b><br><span class="muted">Jenkins checks out the code and prepares the application.</span></div><div class="step"><b>03 · Test</b><br><span class="muted">Automated Python tests verify the Flask endpoints.</span></div><div class="step"><b>04 · Package</b><br><span class="muted">Docker builds a reproducible application image.</span></div><div class="step"><b>05 · Deploy</b><br><span class="muted">The successful artifact can be promoted to the target environment.</span></div></div><div class="card"><h3>Pipeline status</h3><p class="ok">● Ready for CI/CD</p><p class="muted">Use Jenkins to connect this repository and execute the Jenkinsfile.</p></div></main>''')


@app.route("/about")
def about():
    return layout("About", '''<main class="page"><span class="badge">PROJECT</span><h1>Why this demo exists</h1><p>This project is intentionally small so the CI/CD concepts are visible instead of hidden behind a large application.</p><div class="grid"><div class="card"><h3>Application</h3><p class="muted">Python + Flask provides the web layer and health endpoint.</p></div><div class="card"><h3>Automation</h3><p class="muted">Jenkins coordinates repeatable build and test stages.</p></div><div class="card"><h3>Infrastructure</h3><p class="muted">Docker provides a consistent runtime environment.</p></div></div><h2>Example architecture</h2><div class="code">Developer → GitHub → Jenkins → Test → Docker Build → Deployment</div></main>''')


@app.route("/health")
def health():
    return {"status": "healthy", "service": "ci-cd-example"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
