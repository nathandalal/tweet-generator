from tweet_engine import runner
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def only_route():
    f = open('workfile', 'r');
    text = f.read()
    f.close()
    text = "\"" + text + "\""
    return render_template('index.html', tweet=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
