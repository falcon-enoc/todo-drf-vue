from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Task, User, Assign
from .serializers import TaskSerializer, UserSerializer, AssignSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'completed']

class AssignViewSet(viewsets.ModelViewSet):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task', 'user']
