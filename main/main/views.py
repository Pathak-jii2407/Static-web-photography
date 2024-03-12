from django.shortcuts import render

import pandas as pd

def index(request):
    return render(request,'index.html')

def send_data(request):
    name=request.POST.get('name','Invalid')
    email=request.POST.get('email','Invalid')
    phone=request.POST.get('phone','Invalid')
    address=request.POST.get('address','Invalid')
    df=pd.read_csv("{% static 'data\data1.csv'%}")
    print(df)

    print("Data added successfully.")

    return render(request,'index.html')







