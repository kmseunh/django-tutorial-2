from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Task


# Register a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Login a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateTaskForm(ModelForm):

    class Meta:

        model = Task
        fields = ["title", "content"]
        exclude = ["user"]


class UpdateUserForm(ModelForm):

    password = None

    class Meta:

        model = User
        fields = ["username", "email"]
        exclude = ["password1", "password2"]
