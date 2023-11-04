from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.


import re

def is_valid_password(request,password):
    # Check if the password is at least 8 characters long
    is_valid = True
    if len(password) < 6:
        messages.error(request, 'Password should contains minimum 8 characters')
        is_valid = False

    # Check if the password contains at least one uppercase letter (A-Z)
    if not re.search(r'[A-Z]', password):
        messages.error(request, 'Password should Include at least one uppercase letter (A-Z)')
        is_valid = False

    # Check if the password contains at least one lowercase letter (a-z)
    if not re.search(r'[a-z]', password):
        messages.error(request, 'Password should Include at least one lowercase letter (A-Z)')
        is_valid = False

    # Check if the password contains at least one number (0-9)
    if not re.search(r'[0-9]', password):
        messages.error(request, 'Password should Include at least one number (0-9)')
        is_valid = False

    # Check if the password contains at least one special character
    special_characters = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]'
    if not re.search(special_characters, password):
        messages.error(request, 'Include at least one special character')
        is_valid = False

    # Check if the password contains common words or personal information
    common_words = ["password", "123456", "admin"]  # Add more common words here
    for common_word in common_words:
        if common_word in password.lower():
            messages.error(request, 'Avoid common words and personal information')
            is_valid = False

    # All criteria are met, the password is valid
    return is_valid


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
            if not is_valid_password(request,password1):
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