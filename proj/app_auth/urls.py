from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/yandex/', views.YandexLoginView.as_view(), name='yandex-login'),
    path('login/yandex/redirect/', views.YandexLoginRedirectView.as_view(), name='yandex-redirect'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

