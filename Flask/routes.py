from main import app

from flask import request
import json

# Models
from models.treatments import regEmergence, regYield

from helpers.format import formatTreatmentsData, formatSecondTreatmentsData
import numpy as np

# Index
@app.route("/")
def hello_world():
    return "<p>Flask Models</p>"

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
    
    print(json.dumps({
        'success': True,
        'data': {
            'model': 'treatments',
            'yield': yieldResult[0],
            'emergence': emergenceResult[0]
        }
    }))

    return json.dumps({'yield': yieldResult[0], 'emergence': emergenceResult[0]})

# Endpoint for treatments model
@app.route("/treatments/compare", methods=['POST'])
def treatmentsCompare():
    inp = formatTreatmentsData(request);
    secondInp = formatSecondTreatmentsData(request);

    print("inp")
    print(inp)
    print("secondInp")
    print(secondInp)

    # Models
    yieldResult = regYield(np.array([inp]))
    emergenceResult = regEmergence(np.array([inp]))

    secondYieldResult = regYield(np.array([secondInp]))
    secondEmergenceResult = regEmergence(np.array([secondInp]))

    return json.dumps({
        'model': 'treatments compare',
        'yield': {
            'result': yieldResult[0],
            'result2': secondYieldResult[0],
            'difference': (((yieldResult[0] - secondYieldResult[0]) / yieldResult[0]) * 100)
        },
        'emergence': {
            'result': emergenceResult[0],
            'result2': secondEmergenceResult[0],
            'difference': (((emergenceResult[0] - secondEmergenceResult[0]) / emergenceResult[0]) * 100)
        }
    })

# Endpoint for moisture precentage model
@app.route("/moisture-precentage", methods=['POST'])
def moisturePrecentage():
    return json.dumps({'yield': 0, 'emergence': 0})

# Endpoint for bulk density model
@app.route("/bd-moisture", methods=['POST'])
def bulkDensityMoisture():
    return json.dumps({'yield': 0, 'emergence': 0})