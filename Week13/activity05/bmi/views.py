from django.shortcuts import render
from google import genai  # pylint: disable=no-name-in-module
import os
from dotenv import load_dotenv
import markdown

load_dotenv()


def index(request):
    context = {}
    if request.method == 'POST':
        gender = request.POST['gender']
        age = int(request.POST['age'])
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

        diet_n_exercise_plan = get_diet_n_exercise_plan(
            gender, age, height_cm, weight_kg)

        context = {
            'gender': gender,
            'age': age,
            'bmi': bmi,
            'category': category,
            'height': request.POST['height'],
            'weight': request.POST['weight'],
            'diet_n_exercise_plan': diet_n_exercise_plan
        }

    return render(request, 'bmi.html', context)


def get_diet_n_exercise_plan(gender, age, height, weight, months=1):
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    client.config = {
        "temperature": 0.7,
        "topP": 0.95,
        "topK": 40,
        "maxOutputTokens": 1000
    }
    # client.configure(config)

    prompt = (
        f"Create a {months}-month diet and exercise plan for a {age}-year-old {gender} "
        f"who is {height}cm tall and weighs {weight}kg."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return markdown.markdown(response.text)
