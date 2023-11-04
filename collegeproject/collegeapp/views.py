from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request,"index.html")

def signin_page(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect("signin")

    return render(request, "signin.html")

def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Exists")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, "username Already Exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username, email, password1)
                user.save()
                messages.info(request, "Account created successfully")
                return redirect('signin')
        else:
            messages.error(request, "Please Enter same Password")
            return redirect('signup')
    return render(request, "signup.html")

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')