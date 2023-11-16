from flask import Flask
import redis
app = Flask(__name__)

@app.route("/")
def hello_name():
    r = redis.Redis(host="localhost", port=6379, db=0)
    name = r.get("name").decode()
    return "Hello {}\n".format(name)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)