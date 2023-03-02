from django.shortcuts import render,redirect
from .models import Student
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        global user_data
        user_data={
            'password':request.POST['password'],
            'name':request.POST['name'],
            'email':request.POST['email'],
            'mobile':request.POST['mobile']
        }
        global otp
        otp=random.randint(100_000,999_999)
        subject= 'Account Registation'
        massage=f'hello {user_data["name"]}!! \nYour OTP is {otp}.'
        send_mail(subject,massage,settings.EMAIL_HOST_USER,[user_data['email']])
        return render(request,'otp.html')
    
def potp(request):
    if otp==int(request.POST['uotp']):
        sss=Student.objects.create(
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password'],
            mobile=user_data['mobile'],
       )

        sss.save()
        return render(request,'in.html',{'mssg':'Account Successfully!!'})
    else:
        return render(request,'otp.html',{'mssg':'Invalid otp!!'})
    

def show(request):
    sss=Student.objects.all()
    free={
        'sss':sss
    }
    return render(request,'in.html',free)


def delete(request,pk):
    # Student.objects.filter(id=pk).delete()
    Student.objects.get(id=pk).delete()
    return redirect('show')


def edit(request,pk):
    ss=Student.objects.get(id=pk)
    if request.method=='POST':
        ss.name=request.POST['name']
        ss.email=request.POST['email']
        ss.password=request.POST['password']
        ss.mobile=request.POST['mobile']

        ss.save()
        return redirect('show')
    
    return render(request,'edit.html',{'pob':ss})
