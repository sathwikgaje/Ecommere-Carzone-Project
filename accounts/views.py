from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username and password')
            return redirect('login')
    return render(request,'accounts/login.html') 

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                auth.login(request,user)
                user.save()
                messages.success(request,'You registered succesfully')
                messages.success(request,'You are now logged in')
                return redirect('dashboard')

        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html') 

def dashboard(request):
    return render(request,'accounts/dashboard.html') 

def logout_view(request):
    logout(request)
    return redirect('home')