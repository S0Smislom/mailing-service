from django.urls import path
from .views import GeneralStatsView, DetailStatsView, StatsTest

urlpatterns = [
    path('stats/', GeneralStatsView.as_view()),
    path('stats/<int:id>/', DetailStatsView.as_view()),
    path('stats/test/', StatsTest.as_view()),
]