from django.contrib import admin

from .models import LandingPageEntry

class LandingPageEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']

admin.site.register(LandingPageEntry, LandingPageEntryAdmin)