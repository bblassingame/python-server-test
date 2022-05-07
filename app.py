from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Eli!"

@app.route("/user", methods=["POST"])
def user():
    return "user added"

@app.route("/users")
def users():
    return "users returned"