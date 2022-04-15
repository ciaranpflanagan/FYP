# Encode data
def encodeData(data):
    inp = []

    # Prep
    if (data['prep'] == 'ploughed'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Pressure
    if (data['pressure'] == 'high'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Covercrop
    if (data['covercrop'] == 'yes'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Traffic
    if (data['traffic'] == 'high'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Moisture
    if (data['moisture']):
        # Dividing by 31.46666666666667 scales value
        # NOTE: if data changes here this value will need to be updated, need a dynamic way of doing this
        inp.append(float(data['moisture']) / 31.46666666666667)

    return inp

class TreatmentsMoistureFormat:
    # Format data for first model
    def formatTreatmentsData(request):
        # Checking all request params exist
        if (request.form.get('prep') is None
            or request.form.get('pressure') is None
            or request.form.get('moisture') is None
            or request.form.get('covercrop') is None
            or request.form.get('traffic') is None): return False

        data = {
            'prep': request.form.get('prep'),
            'pressure': request.form.get('pressure'),
            'moisture': request.form.get('moisture'),
            'covercrop': request.form.get('covercrop'),
            'traffic': request.form.get('traffic')
        }

        return encodeData(data)

    # Format data for second model
    def formatSecondTreatmentsData(request):
        # Checking all request params exist
        if (request.form.get('prep') is None
            or request.form.get('pressure') is None
            or request.form.get('moisture') is None
            or request.form.get('covercrop') is None
            or request.form.get('traffic') is None
            or request.form.get('changed_attribute') is None
            or request.form.get('changed_val') is None): return False

        data = {
            'prep': request.form.get('prep'),
            'pressure': request.form.get('pressure'),
            'moisture': request.form.get('moisture'),
            'covercrop': request.form.get('covercrop'),
            'traffic': request.form.get('traffic')
        }

        data[request.form.get('changed_attribute')] = request.form.get('changed_val')
        
        return encodeData(data)