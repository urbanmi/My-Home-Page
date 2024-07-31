from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    some_text = "Hello world!"
    current_year = datetime.now().year
    cities = ["Boston", "Washington", "New York"]
    return render_template("index.html", some_text=some_text, current_year=datetime.now().year)

@app.route("/aboutMe")
def aboutMe():
    return render_template("aboutMe.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(use_reloader=False)