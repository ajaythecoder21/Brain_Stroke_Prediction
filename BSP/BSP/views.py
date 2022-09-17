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
    if request.GET['Work Type'] == 'Private':
        val = '1'
    if request.GET['Work Type'] == 'Self-employed':
        val = '2'
    if request.GET['Work Type'] == 'Govt_job':
        val = '0'
    if request.GET['Work Type'] == 'children':
        val = '3'
    lst.append(val)
    lst.append(request.GET['Average Glucose Level'])
    lst.append(request.GET['BMI'])
    if request.GET['Smoking Status'] == 'formerly smoked':
        val = '1'
    if request.GET['Smoking Status'] == 'never smoked':
        val = '2'
    if request.GET['Smoking Status'] == 'smokes':
        val = '3'
    if request.GET['Smoking Status'] == 'Uknown':
        val = '4'
    lst.append(val)
    if request.GET['Gender'] == 'Male':
        val = '1'
    if request.GET['Gender'] == 'Female':
        val = '0'
    lst.append(val)
    if request.GET['Ever Married'] == 'Male':
        val = '1'
    if request.GET['Ever Married'] == 'Female':
        val = '0'
    lst.append(val)
    if request.GET['Residence Type'] == 'Urban':
        val = '1'
    if request.GET['Residence Type'] == 'Rural':
        val = '0'
    lst.append(val)
    print(lst)
    '''
    for val in lst:
        print(val[3])
        if val[3] == 'Private':
            val[3] = '1'
        if val[3] == 'Self-employed':
            val[3] = '2'
        if val[3] == 'Govt_job':
            val[3] = '0'
        if val[3] == 'children':
            val[3] = '3'
        if val[6] == 'formerly smoked':
            val[6] = '1'
        if val[6] == 'never smoked':
            val[6] = '2'
        if val[6] == 'smokes':
            val[6] = '3'
        if val[6] == 'Unknown':
            val[6] = '4'
        if val[7] == 'Male':
            val[7] = '1'
        if val[7] == 'Female':
            val[7] = '0'
        if val[8] == 'Yes':
            val[8] = '1'
        if val[8] == 'No':
            val[8] = '0'
        if val[9] == 'Urban':
            val[9] = '1'
        if val[9] == 'Rural':
            val[9] = '0'
    '''
    y_pred = model.predict([lst])
    if y_pred[0] == 0:
        output = 'Patient NOT DIAGNOSED with Brain Stroke'
        print(y_pred)
        return render(request, 'result.html', {"result": output})
    if y_pred[0] == 1:
        output = 'Patient DIAGNOSED with Brain Stroke'
        print(output)
        return render(request, 'result.html', {"result": output})