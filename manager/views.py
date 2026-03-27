from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Position, Worker, TaskType, Task
from manager import forms


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_workers": Worker.objects.count(),
        "num_tasks": Task.objects.count(),
        "num_positions": Position.objects.count(),
        "num_completed_tasks": Task.objects.filter(is_completed=True).count(),
        "num_open_tasks": Task.objects.filter(is_completed=False).count(),
    }
    return render(request, "manager/index.html", context=context)


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("manager:login")


# Task views
class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = forms.TaskForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = forms.TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


# Worker views
class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = forms.WorkerCreationForm
    success_url = reverse_lazy("manager:login")


# TaskType views
class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = forms.TaskTypeForm
    template_name = "manager/task_type_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = forms.TaskTypeForm
    template_name = "manager/task_type_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_confirm_delete.html"
    context_object_name = "task_type"


# Position views
class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = forms.PositionForm


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = forms.PositionForm


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")
