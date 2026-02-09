from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def profile(request):
#     return HttpResponse("profile page   ")

def profile(request):
    return render(request, 'student/index.html')