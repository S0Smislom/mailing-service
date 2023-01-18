from django.urls import path, include
from rest_framework import routers

from .views import ClientViewSet

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)

urlpatterns = [
    path('', include(router.urls))
]