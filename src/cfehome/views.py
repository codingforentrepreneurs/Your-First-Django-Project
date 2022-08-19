# from django.http import HttpResponse
from django.shortcuts import render

def home_page(request, *args, **kwargs):
    return render(request, "index.html")