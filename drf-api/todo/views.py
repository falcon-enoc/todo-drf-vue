from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, viewsets
from .models import Task, User, Assign, Tag, Board, Project
from .serializers import TaskSerializer, UserSerializer, AssignSerializer, TagSerializer, BoardSerializer, ProjectSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'completed', 'board']

class AssignViewSet(viewsets.ModelViewSet):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task', 'user']

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tag']

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tasks', 'project']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['boards']