from django.urls import path

from .views import (
    createTask,
    deleteTask,
    home,
    my_login,
    register,
    updateTask,
    viewTasks,
)

urlpatterns = [
    path("", home),
    # CRUD - operations
    path("create-task", createTask, name="create-task"),
    path("view-tasks", viewTasks, name="view-tasks"),
    path("update-task/<str:pk>/", updateTask, name="update-task"),
    path("delete-task/<str:pk>/", deleteTask, name="delete-task"),
    # Register a user
    path("register", register, name="register"),
    # Login a user
    path("my-login", my_login, name="my-login"),
]
