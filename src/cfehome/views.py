# from django.http import HttpResponse
from django.shortcuts import render

from .forms import LandingPageForm

def home_page(request, *args, **kwargs):
    title = "Welcome home"
    print(request.method == "POST")
    form = LandingPageForm()
    print(request.POST.get("email"))

    context = {
        "title": title,
        "form": form
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