# Flask is a web framework for Python that allows you to build web applications quickly and easily.
# Flask is lightweight and flexible, making it a popular choice for both beginners and experienced developers.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/stages")
def stages():
    return render_template("stages.html")


@app.route("/hello")
def hello():
    return "Hello from Flask! 🦋"


@app.route("/user/<name>")
def user(name):
    return f"Hi {name}, welcome to the Butterfly World! 🦋"


if __name__ == "__main__":
    app.run(debug=True)
