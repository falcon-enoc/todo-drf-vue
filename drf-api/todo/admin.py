from django.contrib import admin
from .models import Task, User, Assign, Tag, Project, Board

admin.site.register(Task)
admin.site.register(User)
admin.site.register(Assign)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Board)


