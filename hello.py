from flask import Flask
import time
import thread

app = Flask(__name__)

def flaskThread():
    app.run()

@app.route('/')
def hello_world():
    f = open('workfile', 'r');
    text = f.read()
    f.close()
    return render_template()


if __name__ == "__main__":
    thread.start_new_thread(flaskThread,())
