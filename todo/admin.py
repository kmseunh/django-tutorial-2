from django.contrib import admin

from .models import Profile, Task

admin.site.register(Task)
admin.site.register(Profile)
