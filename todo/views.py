from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CreateUserForm, TaskForm
from .models import Task


def home(request):

    return render(request, "index.html")


def my_Login(request):

    return render(request, "my-login.html")


def createTask(request):

    form = TaskForm()

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("view-tasks")

    context = {"form": form}

    return render(request, "create-task.html", context=context)


def viewTasks(request):

    tasks = Task.objects.all()

    context = {"tasks": tasks}

    return render(request, "view-tasks.html", context=context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect("view-tasks")

    context = {"form": form}

    return render(request, "update-task.html", context=context)


def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":

        task.delete()

        return redirect("view-tasks")

    context = {"object": task}

    return render(request, "delete-task.html", context=context)


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponse("The user was registered!")

    context = {"form": form}

    return render(request, "register.html", context=context)
