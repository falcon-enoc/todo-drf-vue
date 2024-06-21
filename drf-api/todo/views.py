from django.shortcuts import render
from rest_framework import generics
from .models import Task, User, Assign
from .serializers import TaskSerializer, UserSerializer, AssignSerializer

# Task Views
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# User Views
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Assign Views
class AssignListCreate(generics.ListCreateAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer