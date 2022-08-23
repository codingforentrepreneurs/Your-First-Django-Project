from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import LandingPageEntry
from .forms import LandingPageEntryModelForm, EntryNotesModelForm



def home_page(request, *args, **kwargs):
    title = "Welcome home"
    form = LandingPageEntryModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Thanks for joining!", extra_tags='alert-success')
        form = LandingPageEntryModelForm()
        request.session['did_submit'] = True
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
    }
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
    form = EntryNotesModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        if not obj.notes_by:
            obj.notes_first_added = timezone.now()
        obj.notes_by = user
        obj.save()
        messages.success(request, f"Entry {obj.id} Updated!", extra_tags='alert-success')
        return HttpResponseRedirect(obj.get_absolute_url())
    context = {
        "object": obj,
        "form": form,
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



def bootstrap_view(request, *args, **kwargs):
    return render(request, "landing_pages/bootstrap.html", {})