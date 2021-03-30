from flask import Flask, request as req, jsonify
import json, time, math, random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home')
def home():
    return 'Home'


@app.route('/api/<domain>')
def apiClass(domain):
    return "your API is %s"%domain


@app.route('/iot', methods = ['POST'])
def iot():
    now = time.time()*10
    current = random.randrange(1,7)
    volt = random.randrange(3,10)
    power = current * volt
    sensorData = {"time": now,
                  "data":
                      {
                          "current" : current,
                          "volt" : volt,
                          "power" : power
                      }

                  }
    # data = req.get_json()
    return json.dumps(sensorData)

if __name__ == "__main__":
    app.run()
