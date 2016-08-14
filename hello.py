from flask import Flask
import threading
import runner
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    f = open('workfile', 'r');
    text = f.read()
    f.close()
    return text
threads = []

def worker():
    runner.run()

if __name__ == "__main__":
    t = threading.Thread(target=worker)
    t.start()
    app.run(host='0.0.0.0')

