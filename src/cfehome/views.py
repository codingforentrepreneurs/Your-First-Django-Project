from django.http import HttpResponse


def home_page(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")