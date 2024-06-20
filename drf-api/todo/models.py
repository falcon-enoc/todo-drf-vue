from django.db import models
from django.utils import timezone

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = [id, 'name']

    def __str__(self):
        # String representation of the To-Do item, useful in the admin interface and elsewhere
        return self.name

