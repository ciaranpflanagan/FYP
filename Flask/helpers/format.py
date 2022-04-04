def formatTreatmentsData(request):
    inp = []
    # Prep
    if (request.form.get('prep') == 'ploughed'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Pressure
    if (request.form.get('pressure') == 'high'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Moisture
    if (request.form.get('moisture') == 'high'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Covercrop
    if (request.form.get('covercrop') == 'yes'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    # Traffic
    if (request.form.get('traffic') == 'high'):
        inp.append(1.0)
        inp.append(0.0)
    else:
        inp.append(0.0)
        inp.append(1.0)

    return inp