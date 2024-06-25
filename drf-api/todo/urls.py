from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename = 'tasks')
router.register('users', UserViewSet, basename = 'users')
router.register('assigns', AssignViewSet, basename = 'assigns')
router.register('tags', TagViewSet, basename = 'tags')

urlpatterns = router.urls

