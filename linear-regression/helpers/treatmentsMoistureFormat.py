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
        inp.append(float(data['moisture']) / 31.46666666666667) # Dividing by 31.46666666666667 scales value

    return inp

class TreatmentsMoistureFormat:
    # Format data for first model
    def formatTreatmentsData(request):
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
        data = {
            'prep': request.form.get('prep'),
            'pressure': request.form.get('pressure'),
            'moisture': request.form.get('moisture'),
            'covercrop': request.form.get('covercrop'),
            'traffic': request.form.get('traffic')
        }

        data[request.form.get('changed_attribute')] = request.form.get('changed_val')
        
        return encodeData(data)