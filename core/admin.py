from django.contrib import admin
from .models import Report, Location

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'location', 'date_reported', 'reporter']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']


