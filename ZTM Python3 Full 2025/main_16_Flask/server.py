# Flask is a web framework for Python that allows you to build web applications quickly and easily.
# Flask is lightweight and flexible, making it a popular choice for both beginners and experienced developers.
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

STAGES = [
    {"key": "Caterpillar", "emoji": "🐛",
     "desc": "Eats leaves and grows rapidly.",
     "img": "caterpillar.png",
     "fact": "A caterpillar has up to 4,000 muscles!"},
    {"key": "Chrysalis", "emoji": "🫧",
     "desc": "Transforms inside the chrysalis.",
     "img": "chrysalis.png",
     "fact": "Organs and tissues are reorganized during metamorphosis."},
    {"key": "Butterfly", "emoji": "🦋",
     "desc": "Emerges and takes flight.",
     "img": "butterfly.png",
     "fact": "Butterflies taste with their feet."}
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/stages")
def stages():
    return render_template("stages.html")


@app.route("/api/stages")
def api_stages():
    out = []
    for s in STAGES:
        out.append({**s, "img": url_for("static", filename=s["img"])})
    return jsonify(out)


@app.route("/hello")
def hello():
    return "Hello from Flask! 🦋"


@app.route("/user/<name>")
def user(name):
    return f"Hi {name}, welcome to the Butterfly World! 🦋"


if __name__ == "__main__":
    app.run(debug=True)
