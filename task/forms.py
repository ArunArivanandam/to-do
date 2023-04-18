from django.forms import ModelForm
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']


User = get_user_model()


class CreateUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', ]
        field_classes = {'username': UsernameField}
