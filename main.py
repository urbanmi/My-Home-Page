from flask import Flask, render_template, request, make_response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    some_text = "Hello world!"
    current_year = datetime.now().year
    cities = ["Boston", "Washington", "New York", "Berlin"]
    return render_template("index.html", some_text=some_text, current_year=datetime.now().year, cities=cities)

@app.route("/aboutMe", methods=["GET", "POST"])
def aboutMe():
    with open("static/aboutMihevc.txt", "r") as aboutFile:
        aboutList = aboutFile.read().splitlines()

    if request.method == "GET":
        name = request.cookies.get("user-name")
        return render_template("aboutMe.html", aboutList=aboutList, name=name)
    if request.method == "POST":
        contact_name = request.form.get("contact-name")
        message = request.form.get("contact-message")
        response = make_response(render_template("success.html"))
        response.set_cookie("user-name", contact_name)
        print("contact_name")
        print("message")
        return response

@app.route("/portfolio")
def portfolio():
    with open("static/portfolio.txt", "r") as portfolioFile:
        portfolioList = portfolioFile.read().splitlines()
        return render_template("portfolio.html", portfolioList=portfolioList)

if __name__ == "__main__":
    app.run(use_reloader=False)