from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from .views import LoginView, RefreshView, GuestUpgradeView


urlpatterns = [
    path("auth/login", LoginView.as_view(), name="auth-login"),
    path("auth/refresh", RefreshView.as_view(), name="auth-refresh"),
    path("auth/verify", TokenVerifyView.as_view(), name="auth-verify"),
    path("auth/guest-upgrade", GuestUpgradeView.as_view(), name="auth-guest-upgrade"),
]
