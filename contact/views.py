from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request, "index.html")

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        lastname=request.POST.get('lastname')
        number=request.POST.get('number')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,lastname,number,email,age,gender)
        query=Student(name=name,lastname=lastname,number=number,email=email,age=age,gender=gender)
        query.save()
    return render(request, "index.html")

def about(request):
    return render(request, "index.html")
