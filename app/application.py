from flask import Flask
import signal
import sys

app = Flask(__name__)

def handle_sigterm(signum, frame):
    print("🟡 Received SIGTERM — cleaning up gracefully...")
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

@app.route("/")
def index():
    return "Hello from resilient container!"

if __name__ == "__main__":
    print("✅ App started — ready to serve on port 8080")
    app.run(host="0.0.0.0", port=8080)
