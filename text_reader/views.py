# text_reader/views.pye

from django.http import HttpResponse


def index(request):
    return HttpResponse('Давай уже ебашь пет, лентяй!')


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)


def contacts(request):
    return HttpResponse("<h2>Контакты</h2>")