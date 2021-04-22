from django.contrib import admin

from .models import Manager, Employee

# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['email','first_name']

admin.site.register(Manager, ManagerAdmin)
admin.site.register(Employee)

