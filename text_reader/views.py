# text_reader/views.pye

from django.http import HttpResponse


def index(request):

    return HttpResponse('<h2>Тут что-то будет</h2>')


def about(request):
    return HttpResponse('<h2>Тут тоже что-то будет</h2>')


def contacts(request):
    return HttpResponse("<h2>И тут тоже </h2>")
