from django.urls import path, include
from rest_framework import routers

from .views import MailingViewSet, TimezoneListView

router = routers.DefaultRouter()
router.register(r'mailing', MailingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('timezones/', TimezoneListView.as_view()),
]