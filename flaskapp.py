from flask import Flask
from sentence_cruncher import runner
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def execute():
	while True:
	    # runner.do_it()
	    time.sleep(300)
	    print '10 more minutes till tweet.'
	    time.sleep(300)
	    print '5 more minutes till tweet.'
	    time.sleep(240)
	    print '1 more minutes till tweet.'
	    time.sleep(60)