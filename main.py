from flask import Flask, render_template, request, make_response, redirect
from datetime import datetime

from sqla_wrapper import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy("sqlite:///db.sqlite")

db_url = os.getenv(os.getenv("DATABASE_URL","sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url)



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)

db.create_all()

@app.route("/")
def index():
    messages = db.query(Message).all()
    return render_template("index.html", messages=messages)

@app.route("/add-message", methods=["POST"])
def add_message():
    username = request.form.get("chat-name")
    text = request.form.get("chat-message")
    message = Message(author=username, text=text)
    message.save()

    return redirect("/")

if __name__ == "__main__":
    app.run(use_reloader=False)