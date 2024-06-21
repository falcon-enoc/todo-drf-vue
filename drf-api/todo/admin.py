from django.contrib import admin
from .models import Task, User, Assign

admin.site.register(Task)
admin.site.register(User)
admin.site.register(Assign)

