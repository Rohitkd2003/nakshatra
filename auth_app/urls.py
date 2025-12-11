from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserView,
    UserUpdateView,
    LogoutView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", UserView.as_view(), name="user-details"),     # ⭐ better naming
    path("update/", UserUpdateView.as_view(), name="user-update"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
