from flask import Flask
from mapstate import MapState

app = Flask(__name__)

ms = MapState()


@app.route("/")
def hello():
    return "Hello World!" + str(ms)
