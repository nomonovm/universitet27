from django.contrib import admin
from mainApp.models import *

class UstozAdmin(admin.ModelAdmin):
    list_display = ["ism", "yosh", "daraja", "fan"]
    list_display_links = ['ism']
    search_fields = ['ism']

class YonalishAdmin(admin.ModelAdmin):
    list_display = ['nom', 'aktiv']
    list_filter = ['aktiv']
    search_fields = ['nom']

class FanAdmin(admin.ModelAdmin):
    list_display = ['nom', 'yonalish', 'asosiy']
    list_filter = ['asosiy', 'yonalish']
    search_fields = ['nom']

admin.site.register(Yonalish , YonalishAdmin)
admin.site.register(Ustoz, UstozAdmin)
admin.site.register(Fan, FanAdmin)
