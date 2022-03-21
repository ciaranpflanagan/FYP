from flask import Flask
from models.treatments import regYield

import numpy as np

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soil-moisture")
def soil_moisture():
    # Interact with Soil Moisture model

    return "<p>Soil Moisture Endpoint</p>"

@app.route("/treatments")
def treatments():
    # Test data
    plot36 = np.array([[1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0]])
    plot55 = np.array([[0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]])

    result = regYield(plot55)

    return "Expected Yield: %s"%(str(result[0]))