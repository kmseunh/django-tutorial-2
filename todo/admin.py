from django.contrib import admin

from .models import Review, Task

admin.site.register(Task)
admin.site.register(Review)
