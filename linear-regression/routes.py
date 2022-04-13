from main import app

from flask import request
import json

# Models
from models.treatments import Treatments
from models.treatments_moisture import TreatmentsMoisture

from helpers.format import formatTreatmentsData, formatSecondTreatmentsData
import numpy as np

# Index
@app.route("/")
def hello_world():
    return "<p>Flask Linear Regression Models</p>"

# Endpoint for treatments model
@app.route("/treatments", methods=['POST'])
def treatments():
    inp = formatTreatmentsData(request);

    # Models
    yieldResult = Treatments.regYield(np.array([inp]))
    emergenceResult = Treatments.regEmergence(np.array([inp]))

    return json.dumps({
        'model': 'treatments',
        'yield': {
            'result': yieldResult[0]
        },
        'emergence': {
            'result': emergenceResult[0]
        }
    })

# Endpoint for treatments model
@app.route("/treatments/compare", methods=['POST'])
def treatmentsCompare():
    inp = formatTreatmentsData(request);
    secondInp = formatSecondTreatmentsData(request);

    # Models
    yieldResult = Treatments.regYield(np.array([inp]))
    emergenceResult = Treatments.regEmergence(np.array([inp]))

    secondYieldResult = Treatments.regYield(np.array([secondInp]))
    secondEmergenceResult = Treatments.regEmergence(np.array([secondInp]))

    return json.dumps({
        'model': 'treatments compare',
        'yield': {
            'result': yieldResult[0],
            'result2': secondYieldResult[0],
            'difference': (((secondYieldResult[0] - yieldResult[0]) / yieldResult[0]) * 100)
        },
        'emergence': {
            'result': emergenceResult[0],
            'result2': secondEmergenceResult[0],
            'difference': (((secondEmergenceResult[0] - emergenceResult[0]) / emergenceResult[0]) * 100)
        }
    })

# Endpoint for treatments moisture model
@app.route("/treatments-moisture", methods=['POST'])
def treatments():
    inp = formatTreatmentsData(request);

    # Models
    yieldResult = TreatmentsMoisture.regYield(np.array([inp]))
    emergenceResult = TreatmentsMoisture.regEmergence(np.array([inp]))

    return json.dumps({
        'model': 'treatments_moisture',
        'yield': {
            'result': yieldResult[0]
        },
        'emergence': {
            'result': emergenceResult[0]
        }
    })

# Endpoint for the treatments moisture model comparison
@app.route("/treatments/compare", methods=['POST'])
def treatmentsCompare():
    inp = formatTreatmentsData(request);
    secondInp = formatSecondTreatmentsData(request);

    # Models
    yieldResult = TreatmentsMoisture.regYield(np.array([inp]))
    emergenceResult = TreatmentsMoisture.regEmergence(np.array([inp]))

    secondYieldResult = TreatmentsMoisture.regYield(np.array([secondInp]))
    secondEmergenceResult = TreatmentsMoisture.regEmergence(np.array([secondInp]))

    return json.dumps({
        'model': 'treatments_moisture compare',
        'yield': {
            'result': yieldResult[0],
            'result2': secondYieldResult[0],
            'difference': (((secondYieldResult[0] - yieldResult[0]) / yieldResult[0]) * 100)
        },
        'emergence': {
            'result': emergenceResult[0],
            'result2': secondEmergenceResult[0],
            'difference': (((secondEmergenceResult[0] - emergenceResult[0]) / emergenceResult[0]) * 100)
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
