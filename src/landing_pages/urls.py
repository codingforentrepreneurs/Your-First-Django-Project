from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing_page_entry_list_view),
]
