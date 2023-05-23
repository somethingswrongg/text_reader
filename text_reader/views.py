from django.shortcuts import render

from django.shortcuts import render


def index(request):
    return render(request, "index.html", context={'body': '<h1>GdsfdhfhD</h1>'})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")