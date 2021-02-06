from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')
def correct(request):
    return render(request,'question0.html')
def quest1(request):
    return render(request,'question1.html')
def ans2(request):
    return render(request,'question2.html')
def right(request):
    return render(request,'rightanswer2.html')
def quest3(request):
    return render(request,'question3.html')
def ans3(request):
    return render(request,'answer3.html')
def quest4(request):
    return render(request,'question4.html')
def ans4(request):
    return render(request,'answer4.html')
def all(request):
    return render(request,'allinone.html')


