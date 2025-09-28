# Flask is a web framework for Python that allows you to build web applications quickly and easily.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<username>")
def hello_world(username=None):
    return render_template("index.html", name=username)


@app.route("/about")
def ho():
    return render_template("about.html")


@app.route("/hello")
def hello():
    return "Hello routeeeeeeeeeeeee!"


@app.route("/user/<name>")
def user(name):
    return f"Hi, youu goood {name}!"


if __name__ == "__main__":
    app.run(debug=True)   # pornește după ce TOATE rutele sunt definite
