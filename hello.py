from tweet_engine import runner

from flask import Flask, render_template
import threading
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    f = open('workfile', 'r');
    text = f.read()
    f.close()
    text = "\"" + text + "\""
    return render_template('index.html', tweet=text)
threads = []

def worker():
    runner.run()

if __name__ == "__main__":
    t = threading.Thread(target=worker)
    t.start()
    app.run(host='0.0.0.0')

