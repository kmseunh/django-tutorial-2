from django.urls import path

from .views import dashboard, home, my_login, register, user_logout

urlpatterns = [
    path("", home, name=""),
    # Register a user
    path("register", register, name="register"),
    # Login a user
    path("my-login", my_login, name="my-login"),
    # Dashboard page
    path("dashboard", dashboard, name="dashboard"),
    # Logout a user
    path("user-logout", user_logout, name="user-logout"),
]
