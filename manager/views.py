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


class TaskListView(generic.ListView):
    model = Task
