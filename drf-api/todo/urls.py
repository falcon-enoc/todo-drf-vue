from django.urls import path
from .views import *

urlpatterns = [
    path('tareas/', TaskListCreate.as_view(), name='task-list'),
    path('tareas/<int:pk>', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('assings/', AssignListCreate.as_view(), name='assing-list'),
    path('assings/<int:pk>', AssignRetrieveUpdateDestroy.as_view(), name='assing-detail'),
]
