from django.shortcuts import render


def home(request):
    if request.method == "GET":
        return render(request, "home.html")

    elif request.method == "POST":
        pass
