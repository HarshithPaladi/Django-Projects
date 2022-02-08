from typing import Counter
from django.http.response import HttpResponseGone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from student.models import *

'''
def get_subject(request,code):
    mark_data = [
        {"code":1,"name":"maths","Marks":10},
        {"code":2,"name":"science","Marks":23},
        {"code":3,"name":"english","Marks":25},
        {"code":4,"name":"TOC","Marks":21}
    ]
    name_r = None
    marks_r = None
    for i in mark_data:
        if i["code"] == code:
            name_r =  i["name"]
            marks_r = i["Marks"]
    if name_r is None:
        return TemplateResponse(request,"index_code.html" ,context = {"Error" : "ERROR DHOLARE"})
    return TemplateResponse(request , "index_code.html", context = {"Name" : name_r , "Marks" : marks_r})
        
def index(request):
    mark_data = [
        {"code":1,"name":"maths","Marks":10},
        {"code":2,"name":"science","Marks":23},
        {"code":3,"name":"english","Marks":25},
        {"code":4,"name":"TOC","Marks":21}
    ]
    summ = 0
    for i in mark_data:
        summ += i["Marks"]
    averg = summ/len(mark_data)

    return TemplateResponse(request, "index.html",context = { "name" :"LOOOLLL","marks":mark_data,"sum":summ,"average":averg})
    '''
def index(request):
    return TemplateResponse( request , "index.html")

def student_dash(request):
    if request.method == "GET":
        students = Student.objects.all()
        return TemplateResponse(request , "student.html", context={"students": students})

def create_stud(request):
    if request.method == "GET":
        d = Dept.objects.all()
        return TemplateResponse(request, "create_students.html" , context = {"departments":d})
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        dept = request.POST.get("dept", None)

        if not name:
            return HttpResponse("Name cant be empty")
        elif not dept:
            return HttpResponse("Dept cant be empty")
        
        try:
            d = Dept.objects.get(id = dept)
        except:
            return HttpResponse("Dept has ntg")
        s = Student(name = name , dept = d)
        s.save()

        return HttpResponseRedirect(reverse("student_dashboard"))
    else:
        return HttpResponse("Invalid Request")


def teacher_dash(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        return TemplateResponse(request , "teacher.html", context={"teachers": teachers})

def create_teach(request):
    if request.method == "GET":
        d = Dept.objects.all()
        return TemplateResponse(request, "create_teachers.html" , context = {"departments":d})
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        dept = request.POST.get("dept", None)

        if not name:
            return HttpResponse("Name cant be empty")
        elif not dept:
            return HttpResponse("Dept cant be empty")
        
        try:
            d = Dept.objects.get(id = dept)
        except:
            return HttpResponse("Dept has ntg")
        t = Teacher(name = name , dept = d)
        t.save()

        return HttpResponseRedirect(reverse("teacher_dashboard"))
    else:
        return HttpResponse("Invalid Request")


def course_dash(request):
        if request.method == "GET":
            courses =  course.objects.all()
            return TemplateResponse(request , "course.html", context={"courses": courses})

def  create_enroll(request):
    if request.method == "GET":
        tc = Teacher.objects.all()
        st = Student.objects.all()
        sb = Subject.objects.all()
        return TemplateResponse(request, "create_courses.html" , context = {"teachers":tc , "students":st, "subjects":sb})
    
    if request.method == "POST":
        student = request.POST.get("student", None)
        teacher = request.POST.get("teacher", None)
        subject = request.POST.get("subject" , None)
        
        try:
            student = Student.objects.get(id=student)
            teacher = Teacher.objects.get(id=teacher)
            subject = Subject.objects.get(id=subject)
        except:
            return HttpResponse("Invalid data")
        
        if student.dept.id != teacher.dept.id:
            return HttpResponse("Student and Teacher dept are not the same")

        if course.objects.filter(student=student, subject=subject).exists():
            return HttpResponse("Course already enrolled")
        
        if course.objects.filter(teacher=teacher).count() >= 60:
            return HttpResponse("Teacher unavailable")

        c = course(student=student, teacher=teacher, subject=subject)
        c.save()

        return HttpResponseRedirect(reverse('course_dashboard'))

def student_id(request, studid):
   
    try:
        student = Student.objects.get(id=studid)
    except:
        return HttpResponse ("ID ille")

    if request.method == 'GET':
        d = Dept.objects.all()

        return TemplateResponse(request , 'student_edit.html' , context ={"student": student , "departments":d})
    
    if request.method =="POST":
        try :
            dept = Dept.objects.get(id = request.POST.get("dept", None))
        except:
            HttpResponse("ID ille ")
        student.name = request.POST.get("name", None)
        student.dept = dept
        student.save()
        return HttpResponseRedirect(reverse("student_dashboard"))
    else:
        return HttpResponse("Invalid Request")

