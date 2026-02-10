from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from student.models import Student
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

    student_data = Student.objects.all()
    print(student_data)
    return render(request, 'student/index.html',{"marks":marks,"age":22,"name":"samaul islam","list":[1,2,3,4,5,6],"fruits":["apple","banana","orange"],"student_list":student_data})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/student/profile')
def add_student(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        father_name = request.POST.get("father_name")
        student = Student(name=name, roll=roll, father_name=father_name)
        student.save()
        return redirect('/student/profile')

    return redirect('/student/profile')

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.father_name = request.POST.get('father_name')
        student.save()
        return redirect('/student/profile')
    return render(request, 'student/edit.html', {'student': student})