from django.shortcuts import render,HttpResponse
from .models import employe,role,Department
from django.db.models import Q
from datetime import datetime

def index(request):
    return render(request,'index.html')

def view_all_emp(request):
    emps=employe.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method== "POST":
         first_name=request.POST['first_name']
         last_name = request.POST['last_name']
         salary = request.POST['salary']
         bonus = int(request.POST['bonus'])
         phone = int(request.POST['phone'])
         dept = int(request.POST['dept'])
         role = int(request.POST['role'])
         new_emp=employe(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,phone=phone,role_id=role,hire_date=datetime.now())
         new_emp.save()
         return HttpResponse("Employee add successfully")
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An exception occured")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=employe.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return  HttpResponse('Employee removed succesfully')
        except:
            return HttpResponse('Please Enter valid Emp ID')
    emps=employe.objects.all()
    context={
        "emps":emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=employe.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) or Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An exceptions occurs")

# Create your views here.
