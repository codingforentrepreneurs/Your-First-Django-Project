from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

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


# @login_required
# @staff_member_required
def landing_page_entry_list_view(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You must log in first", status=400)
    if not user.is_staff:
        return HttpResponse("You must be staff", status=400)
    qs = LandingPageEntry.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "landing_pages/list.html", context)


def landing_page_entry_detail_view(request, id, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You must log in first", status=400)
    if not user.is_staff:
        return HttpResponse("You must be staff", status=400)
    obj = get_object_or_404(LandingPageEntry, id=id)
    # obj = LandingPageEntry.objects.get(id=id)
    # obj = LandingPageEntry.objects.get(notes_by=user) # Object or None or Raise ERROR
    # try:
    #     obj = LandingPageEntry.objects.get(notes_by=user)
    # except LandingPageEntry.DoesNotExist:
    #     raise Http404
    # except LandingPageEntry.MultipleObjectsReturned:
    #     obj = LandingPageEntry.objects.filter(notes_by=user).first()
    context = {
        "object": obj
    }
    return render(request, "landing_pages/detail.html", context)


def entry_list_notes_view(request, *args, **kwargs):
    qs = LandingPageEntry.objects.none()
    user = request.user # cfe user, user 1
    # qs = LandingPageEntry.objects.filter(notes_by=user)
    if user.is_authenticated:
        qs = LandingPageEntry.objects.filter(notes_by=user) # []
    context = {
        "object_list": qs
    }
    return render(request, "landing_pages/list.html", context)

