from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "login.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
