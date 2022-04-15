from main import app

from flask import request, Response
import json

# Models
from models.treatments import Treatments
from models.treatments_moisture import TreatmentsMoisture

# Helpers
from helpers.treatmentsFormat import TreatmentsFormat
from helpers.treatmentsMoistureFormat import TreatmentsMoistureFormat
import numpy as np

# Index
@app.route("/")
def hello_world():
    return "<p>Flask Linear Regression Models</p>"

# Endpoint for treatments model
@app.route("/treatments", methods=['POST'])
def treatments():
    inp = TreatmentsFormat.formatTreatmentsData(request);

    # Return 422 error is data missing
    if (inp == False):
        return Response(json.dumps({
            'success': False
        }), status=422, mimetype='application/json')
    
    # Models
    yieldResult = Treatments.regYield(np.array([inp]))
    emergenceResult = Treatments.regEmergence(np.array([inp]))

    return Response(json.dumps({
        'model': 'treatments',
        'yield': {
            'result': yieldResult[0]
        },
        'emergence': {
            'result': emergenceResult[0]
        }
    }), status=200, mimetype='application/json')

# Endpoint for treatments model
@app.route("/treatments/compare", methods=['POST'])
def treatmentsCompare():
    inp = TreatmentsFormat.formatTreatmentsData(request);
    secondInp = TreatmentsFormat.formatSecondTreatmentsData(request);

    # Return 422 error is data missing
    if (inp == False or secondInp == False):
        return Response(json.dumps({
            'success': False
        }), status=422, mimetype='application/json')

    # Models
    yieldResult = Treatments.regYield(np.array([inp]))
    emergenceResult = Treatments.regEmergence(np.array([inp]))

    secondYieldResult = Treatments.regYield(np.array([secondInp]))
    secondEmergenceResult = Treatments.regEmergence(np.array([secondInp]))

    return Response(json.dumps({
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
    }), status=200, mimetype='application/json')

# Endpoint for treatments moisture model
@app.route("/treatments-moisture", methods=['POST'])
def treatmentsMoisture():
    inp = TreatmentsMoistureFormat.formatTreatmentsData(request);

    # Return 422 error is data missing
    if (inp == False):
        return Response(json.dumps({
            'success': False
        }), status=422, mimetype='application/json')

    # Models
    yieldResult = TreatmentsMoisture.regYield(np.array([inp]))
    emergenceResult = TreatmentsMoisture.regEmergence(np.array([inp]))

    return Response(json.dumps({
        'model': 'treatments_moisture',
        'yield': {
            'result': yieldResult[0]
        },
        'emergence': {
            'result': emergenceResult[0]
        }
    }), status=200, mimetype='application/json')

# Endpoint for the treatments moisture model comparison
@app.route("/treatments-moisture/compare", methods=['POST'])
def treatmentsMoistureCompare():
    inp = TreatmentsMoistureFormat.formatTreatmentsData(request);
    secondInp = TreatmentsMoistureFormat.formatSecondTreatmentsData(request);
    
    # Return 422 error is data missing
    if (inp == False or secondInp == False):
        return Response(json.dumps({
            'success': False
        }), status=422, mimetype='application/json')

    # Models
    yieldResult = TreatmentsMoisture.regYield(np.array([inp]))
    emergenceResult = TreatmentsMoisture.regEmergence(np.array([inp]))

    secondYieldResult = TreatmentsMoisture.regYield(np.array([secondInp]))
    secondEmergenceResult = TreatmentsMoisture.regEmergence(np.array([secondInp]))

    return Response(json.dumps({
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
    }), status=200, mimetype='application/json')

# Endpoint for moisture precentage model
@app.route("/moisture-precentage", methods=['POST'])
def moisturePrecentage():
    return Response(json.dumps({
        'yield': 0,
        'emergence': 0
    }), status=200, mimetype='application/json')

# Endpoint for bulk density model
@app.route("/bd-moisture", methods=['POST'])
def bulkDensityMoisture():
    return Response(json.dumps({
        'yield': 0,
        'emergence': 0
    }), status=200, mimetype='application/json')
