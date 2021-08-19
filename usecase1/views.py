from django.http import HttpResponse
from django.shortcuts import render
import joblib
import random
import pandas as pd


def home(request):
    return render(request,"home.html")

def result(request):
    cls = joblib.load('our_model.sav')
    data={
        #'id': random.randint(10000,999999),
        'sex': request.GET['sex'],
        'age' : request.GET['age'],
        'bmi' : request.GET['BMI'],
        'children' : request.GET['children'],
        'smoker' : request.GET['smoking'],
        'region' : request.GET['region'],
        #'charges' : request.GET['Charges'],
        
    }
    print(data)
    index = [1]
    df = pd.DataFrame(data,index)
    print(df)
    df.loc[df['sex'] == 'Male', 'sex'] = 1
    df.loc[df['sex'] == 'Female', 'sex'] = 0

    df.loc[df['smoker'] == 'yes', 'smoker'] = 1
    df.loc[df['smoker'] == 'no', 'smoker'] = 0

    df.loc[df['region'] == 'southwest', 'region'] = 1
    df.loc[df['region'] == 'southeast', 'region'] = 2
    df.loc[df['region'] == 'northwest', 'region'] = 3
    df.loc[df['region'] == 'northeast', 'region'] = 4

    print(df)

    ans  = cls.predict(df)
    if ans[0]<=0:
        ans=ans*(-1)
    value="The predicted medical cost of the customer is "+str(ans[0])
    return render(request,'result.html' , {'message' : value})  

    



