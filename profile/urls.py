from rest_framework import routers
from .views import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('profile', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]