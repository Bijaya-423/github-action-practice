# this code is form https://github.com/LondheShubham153/flask-app-ecs/tree/main
# flask app
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")


@app.route("/health")
def health():
  return "Server is up and running."
