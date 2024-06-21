from django.db import models
from django.utils import timezone

class Task(models.Model):
    HIGH = 'High'
    LOW = 'Low'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (LOW, 'Low'),
    ]

    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_time = models.DateTimeField(null=True, blank=True)
    tags = models.JSONField(default=list)  # Requires Django 3.1+
    refeer_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='related_tasks')
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['title']

    def __str__(self):
        return self.title
    

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def __str__(self):
        return self.username


class Assign(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')

    class Meta:
        verbose_name = 'Asignación'
        verbose_name_plural = 'Asignaciones'
        unique_together = ('task', 'user')

    def __str__(self):
        return f'{self.user.username} -> {self.task.title}'

