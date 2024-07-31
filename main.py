from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    some_text = "Hello world!"
    current_year = datetime.now().year
    cities = ["Boston", "Washington", "New York", "Berlin"]
    return render_template("index.html", some_text=some_text, current_year=datetime.now().year, cities=cities)

@app.route("/aboutMe")
def aboutMe():
    with open("static/aboutMihevc.txt", "r") as aboutFile:
        aboutList = aboutFile.read().splitlines()
    return render_template("aboutMe.html", aboutList=aboutList)

@app.route("/portfolio")
def portfolio():
    with open("static/portfolio.txt", "r") as portfolioFile:
        portfolioList = portfolioFile.read().splitlines()
        return render_template("portfolio.html", portfolioList=portfolioList)

if __name__ == "__main__":
    app.run(use_reloader=False)