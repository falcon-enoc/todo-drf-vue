from django.urls import path
from .views import TodoList, TodoDetail

urlpatterns = [
    path('tareas/', TodoList.as_view(), name='todo-list'),
    path('tareas/<int:pk>', TodoDetail.as_view(), name='todo-detail'),
]
