import os

from flask import Flask, render_template, request, make_response, redirect
from datetime import datetime

from sqla_wrapper import SQLAlchemy
from sqlalchemy_pagination import paginate

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL","sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)

db = SQLAlchemy(db_url)



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)

db.create_all()

@app.route("/")
def index():
    page = request.args.get("page")
    if not page:
        page = 1

    messages_query = db.query(Message)
    messages = paginate(query=messages_query, page=int(page), page_size=5)
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