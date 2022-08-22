# from django.http import HttpResponse
from django.shortcuts import render

from .models import LandingPageEntry
from .forms import LandingPageEntryModelForm

def home_page(request, *args, **kwargs):
    # GET
    # POST
    title = "Welcome home"
    # print(request.method == "POST")
    form = LandingPageEntryModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        print(obj)
        # print(form.cleaned_data)
        # name = form.cleaned_data.get("name")
        # email = form.cleaned_data.get("email")
        # obj = LandingPageEntry.objects.create(name=name, email=email)
        # obj.email = email
        # obj.save()
        
        # obj2 = LandingPageEntry()
        # obj2.name = name
        # obj2.email = email
        # obj2.save()

        form = LandingPageEntryModelForm()
    # print("your email is", request.POST.get("email"))

    context = {
        "title": title,
        "form": form
    }
    # parag = "{title} Justin!".format(**context)
    return render(request, "landing_pages/home.html", context)



def landing_page_entry_list_view(request, *args, **kwargs):
    qs = LandingPageEntry.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "landing_pages/list.html", context)

