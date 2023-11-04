from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page, name="home"),
    path("signin",views.signin_page, name="signin"),
    path("signup",views.signup_page, name="signup"),
    path("logout", views.logout, name="logout")
]
