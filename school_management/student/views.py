from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def profile(request):
#     return HttpResponse("profile page   ")

def profile(request):
    user_data={

        "name":"samaul islam",
        "age":6,
    }

    marks =[
        {
            "id":1,
            "subject":"math",
            "marks":80
        },
        {    "id":2,   
            "subject":"english",
            "marks":90
        },
        {
            "id":3, 
            "subject":"bangla",
            "marks":85
        },{
                "id":4,
            "subject":"science",
            "marks":75
        },{
                "id":5,
            "subject":"social science",
            "marks":70  
        },{
                "id":6,
            "subject":"religion",
            "marks":75
        }
]
    user_data["marks"] = marks
    return render(request, 'student/index.html',{"marks":marks,"age":22,"name":"samaul islam","list":[1,2,3,4,5,6],"fruits":["apple","banana","orange"]})