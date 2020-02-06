from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='HelloViewSet')

urlpatterns = [
    path('', include(router.urls)),
]
