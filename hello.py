from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    f = open('workfile', 'r');
    text = f.read()
    f.close()
    return text

if __name__ == "__main__":
    app.run()
