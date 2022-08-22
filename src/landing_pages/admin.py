from django.contrib import admin

from .models import LandingPageEntry

class LandingPageEntryAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'timestamp']
    search_fields = ['name', 'email']
    readonly_fields = ['name', 'email', 'timestamp'] # 'updated']
    list_filter = ['timestamp']

admin.site.register(LandingPageEntry, LandingPageEntryAdmin)