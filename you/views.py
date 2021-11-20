from django.shortcuts import render

# Create your views here.

def Time(request):
    return render(request, 'apple.html')

def Hai(request):
    return render(request, 'apple.html')

def Go(request):
    return render(request, 'grape.html')    
