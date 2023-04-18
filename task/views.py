from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm, CreateUserCreationForm
from django.core.mail import send_mail
from django.views import generic


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CreateUserCreationForm

    def get_success_url(self):
        return reverse("login")


def list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'list.html', context)


def detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task
    }
    return render(request, 'detail.html', context)


def create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject="A task has been created",
                message="Go to the list to see it",
                from_email="test@test.com",
                recipient_list=["test2@test.com"]
            )
            return redirect(reverse('todos:list'))

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('todos:list'))

    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect(reverse('todos:list'))
