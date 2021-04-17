from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def Homepage(request):
    return render (request,'Homepage.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['uname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, "Username Already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name,
                                                    password=password2)
                user.save()
                messages.success(request,'Registration success')
                return redirect('login')

        else:
            messages.error(request,"Incorrect password. Re-enter again ")
            return redirect('register')
    else:
        return render(request,'Sign_up.html')

def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            s="<h2 style='font-weight:bold;text-align:center;color:blue;font-size:50px;'>Welcome to GGSH<h2>"
            return HttpResponse(s)
        else:
            messages.error(request,'Incorrect Username or password')
            return redirect('login')
    else:
        return render(request,"login.html")
