import json
from random import random, seed
import time
from datetime import datetime

from flask import Flask, Response, render_template

app = Flask(__name__)
seed()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sensor-data')
def sensor_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%d-%m-%y %H:%M:%S'), 
				'value1': random() * 100 , 
				'value2': random() * 100 ,
				'value3': random() * 100 , 
				'value4': random() * 100
				})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001, debug=True, threaded=True)