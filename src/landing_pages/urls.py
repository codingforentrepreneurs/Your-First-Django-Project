from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing_page_entry_list_view),
    path("notes/", views.entry_list_notes_view),
]
