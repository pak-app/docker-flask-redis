from flask import Flask
import redis
app = Flask(__name__)

@app.route("/")
def hello_name():
    r = redis.Redis()
    pass