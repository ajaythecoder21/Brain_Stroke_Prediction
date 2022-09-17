from django.shortcuts import render
from django.http import JsonResponse
import joblib
def home(request):
    return render(request, 'main.html')


def result(request):
    model = joblib.load('model.pkl')
    lst = []
    lst.append(request.GET['Age'])
    lst.append(request.GET['Hypertension'])
    lst.append(request.GET['Heart Disease'])
    lst.append(request.GET['Work Type'])
    lst.append(request.GET['Average Glucose Level'])
    lst.append(request.GET['BMI'])
    lst.append(request.GET['Smoking Status'])
    lst.append(request.GET['Gender'])
    lst.append(request.GET['Ever Married'])
    lst.append(request.GET['Residence Type'])
    print(lst)
    y_pred = model.predict([lst])
    if y_pred[0] == 0:
        output = 'Patient NOT DIAGNOSED with Brain Stroke'
        print(y_pred)
        return render(request, 'result.html', {"result": output})
    elif y_pred[0] == 1:
        output = 'Patient DIAGNOSED with Brain Stroke'
        print(output)
        return render(request, 'result.html', {"result": output})