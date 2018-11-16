from django.contrib import admin
from .models import grouptable,todolist,work_details,people_project
# Register your models here.
admin.site.register(grouptable)
admin.site.register(todolist)
admin.site.register(work_details)
admin.site.register(people_project)
