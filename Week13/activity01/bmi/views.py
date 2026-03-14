from django.shortcuts import render


def index(request):
    context = {}
    if request.method == 'POST':
        height_cm = float(request.POST['height'])
        weight_kg = float(request.POST['weight'])
        height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 1)

        if bmi < 18.5:
            category = 'Underweight'
        elif bmi < 25:
            category = 'Normal weight'
        elif bmi < 30:
            category = 'Overweight'
        else:
            category = 'Obese'

        context = {
            'bmi': bmi,
            'category': category,
            'height': request.POST['height'],
            'weight': request.POST['weight'],
        }
    return render(request, 'bmi.html', context)
