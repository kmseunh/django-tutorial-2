from django.urls import path

from .views import (
    create_task,
    dashboard,
    delete_task,
    home,
    my_login,
    profile_management,
    register,
    update_task,
    user_logout,
    view_tasks,
)

urlpatterns = [
    path("", home, name=""),
    # Register a user
    path("register", register, name="register"),
    # Login a user
    path("my-login", my_login, name="my-login"),
    # Logout a user
    path("user-logout", user_logout, name="user-logout"),
    # Dashboard page
    path("dashboard", dashboard, name="dashboard"),
    # Create a task
    path("create-task", create_task, name="create-task"),
    # Read a task
    path("view-tasks", view_tasks, name="view-tasks"),
    # Update a task
    path("update-task/<str:pk>/", update_task, name="update-task"),
    # Delete a task
    path("delete-task/<str:pk>/", delete_task, name="delete-task"),
    # Profile Management
    path("profile-management", profile_management, name="profile-management"),
]
