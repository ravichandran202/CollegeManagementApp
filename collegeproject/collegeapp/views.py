from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request,"index.html")

def signin_page(request):
    return render(request, "signin.html")

def signup_page(request):
    return render(request, "signup.html")