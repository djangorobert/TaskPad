from django.contrib import admin

# Register your models here.
from tasklist.models import Task

admin.site.register(Task)