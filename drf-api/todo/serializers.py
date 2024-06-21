from rest_framework import serializers
from .models import Task, User, Assign

class TaskSerializer(serializers.ModelSerializer):
    refeer_task_title = serializers.CharField(source='refeer_task.title', read_only=True)  # Campo adicional para mostrar el título de la tarea referida
    related_tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Lista de IDs de tareas relacionadas
    assignments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Lista de IDs de asignaciones

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'priority', 'completed', 'active', 'description',
            'created_at', 'updated_at', 'deadline_time', 'tags', 'refeer_task',
            'refeer_task_title', 'related_tasks', 'level', 'assignments'
        ]
        read_only_fields = ['created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    assignments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Lista de IDs de asignaciones

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'apellido', 'role', 'assignments']


class AssignSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source='task.title', read_only=True)  # Campo adicional para mostrar el título de la tarea
    user_username = serializers.CharField(source='user.username', read_only=True)  # Campo adicional para mostrar el nombre de usuario

    class Meta:
        model = Assign
        fields = ['id', 'task', 'task_title', 'user', 'user_username']