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


# Task views
class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = forms.TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = forms.TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


# Worker views
class WorkerListView(generic.ListView):
    model = Worker


class WorkerDetailView(generic.DetailView):
    model = Worker


# TaskType views
class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type"


# Position views
class PositionListView(generic.ListView):
    model = Position


class PositionDetailView(generic.DetailView):
    model = Position


class PositionCreateView(generic.CreateView):
    model = Position
    form_class = forms.PositionForm


class PositionUpdateView(generic.UpdateView):
    model = Position
    form_class = forms.PositionForm


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")
