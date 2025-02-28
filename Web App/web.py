from flask import Flask

# Run the app
# python -m flask --app web run

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"