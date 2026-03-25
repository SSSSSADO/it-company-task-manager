from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from manager.models import Position, Worker, TaskType, Task


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


# Position views
class PositionListView(generic.ListView):
    model = Position
