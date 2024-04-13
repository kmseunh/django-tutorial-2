from django.urls import path

from .views import (
    createTask,
    deleteTask,
    home,
    my_Login,
    register,
    updateTask,
    viewTasks,
)

urlpatterns = [
    path("my-login", my_Login),
    path("", home),
    # CRUD - operations
    path("create-task", createTask, name="create-task"),
    path("view-tasks", viewTasks, name="view-tasks"),
    path("update-task/<str:pk>/", updateTask, name="update-task"),
    path("delete-task/<str:pk>/", deleteTask, name="delete-task"),
    # Register a user
    path("register", register, name="register"),
]
