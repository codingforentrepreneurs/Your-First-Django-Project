# from django.http import HttpResponse
from django.shortcuts import render

def home_page(request, *args, **kwargs):
    title = "Welcome home"
    context = {
        "title": title
    }
    # parag = "{title} Justin!".format(**context)
    return render(request, "home.html", context)

def abc_page(request, *args, **kwargs):
    title = "ABC"
    context = {
        "title": title
    }
    # parag = "{title} Justin!".format(**context)
    return render(request, "home.html", context)