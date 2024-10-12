from django.shortcuts import render,redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from .models import CustomUser,Usermember
# Create your views here.

def admin1(request):
    return render(request,'admin.html')

def about(request):
    return render(request,'about.html')
def teacher(request):
    return render(request,'teacher.html')

def student(request):
    return render(request,'student.html')

def studentreg(request):
    return render(request,'studentreg.html')

def teacherreg(request):
    return render(request,'teacherreg.html')

def doregister(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        user_name = request.POST['uname']
        last_name = request.POST['lname']
        email_id = request.POST['email']
        age = request.POST[ 'age' ]
        contact = request.POST['contact']
        image = request.FILES.get('image')
        password = request.POST['password']
        user_type = request.POST['text']
        if CustomUser.objects.filter(username=user_name).exists():
            messages.info(request, 'This username already exists!!!!!')
            return redirect('doregister')
        else:
            user=CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,password=password,email=email_id,user_type=user_type)
            user.save()


            member=Usermember(age=age,number=contact,image=image,user=user)
            member.save()
            
            return redirect('/')
    return render(request,'studentreg.html') 

def pregisteration(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        user_name = request.POST['uname']
        last_name = request.POST['lname']
        email_id = request.POST['email']
        age = request.POST[ 'age' ]
        contact = request.POST['contact']
        image = request.FILES.get('image')
        password = request.POST['password']
        user_type = request.POST['text']
        if CustomUser.objects.filter(username=user_name).exists():
            messages.info(request, 'This username already exists!!!!!')
            return redirect('preregisteration')
        else:
            user=CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,password=password,email=email_id,user_type=user_type)
            user.save()


            member=Usermember(age=age,number=contact,image=image,user=user)
            member.save()
            
            return redirect('/')
    return render(request,'teacherreg.html') 

def login1(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        password1=request.POST.get('password')
        user=auth.authenticate(username=user_name,password=password1)


        if user is not None:
            if user.user_type == '1':
                login(request,user)
                return redirect('admin1')
            elif user.user_type == '2':
                auth.login(request,user)
                return redirect('student')
            else:
                auth.login(request,user)
                return redirect('teacher')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('/')
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
            