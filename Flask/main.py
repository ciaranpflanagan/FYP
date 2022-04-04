from flask import Flask
from flask_cors import CORS
from flask import request
import json

# Models
from models.treatments import regEmergence, regYield
from helpers.format import formatTreatmentsData
import numpy as np

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def hello_world():
    return "<p>Flask Models</p>"

@app.route("/soil-moisture")
def soil_moisture():
    # Interact with Soil Moisture model

    return "<p>Soil Moisture Endpoint</p>"

# Endpoint for treatments model
@app.route("/treatments", methods=['POST'])
def treatments():
    inp = formatTreatmentsData(request);
    
    # Test data
    plot36 = np.array([[1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0]])
    plot55 = np.array([[0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]])

    print('inp')
    print(inp)

    # Models
    yieldResult = regYield(np.array([inp]))
    emergenceResult = regEmergence(np.array([inp]))

    return json.dumps({'yield': yieldResult[0], 'emergence': emergenceResult[0]})

# Endpoint for moisture precentage model
@app.route("/moisture-precentage", methods=['POST'])
def moisturePrecentage():
    return json.dumps({'yield': 0, 'emergence': 0})

# Endpoint for bulk density model
@app.route("/bd-moisture", methods=['POST'])
def bulkDensityMoisture():
    return json.dumps({'yield': 0, 'emergence': 0})