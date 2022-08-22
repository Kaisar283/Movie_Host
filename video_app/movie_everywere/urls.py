from django.urls import path
from rest_framework.routers import DefaultRouter
from .Views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [] + router.urls