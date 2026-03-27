from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
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
    template_name = "manager/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        qs = super().get_queryset()
        form = forms.TaskFilterForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data.get("q")
            if q:
                qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

            is_completed = form.cleaned_data.get("is_completed")
            if is_completed == "1":
                qs = qs.filter(is_completed=True)
            elif is_completed == "0":
                qs = qs.filter(is_completed=False)

            priority = form.cleaned_data.get("priority")
            if priority:
                qs = qs.filter(priority=priority)

            task_type = form.cleaned_data.get("task_type")
            if task_type:
                qs = qs.filter(task_type=task_type)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = forms.TaskFilterForm(self.request.GET)
        return context


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
    context_object_name = "worker_list"

    def get_queryset(self):
        qs = super().get_queryset()
        form = forms.WorkerFilterForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data.get("q")
            if q:
                qs = qs.filter(username__icontains=q)
            position = form.cleaned_data.get("position")
            if position:
                qs = qs.filter(position=position)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = forms.WorkerFilterForm(self.request.GET)
        return context


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

    def get_queryset(self):
        qs = super().get_queryset()
        form = forms.TaskTypeFilterForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data.get("q")
            if q:
                qs = qs.filter(name__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = forms.TaskTypeFilterForm(self.request.GET)
        return context



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
    context_object_name = "position_list"

    def get_queryset(self):
        qs = super().get_queryset()
        form = forms.PositionFilterForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data.get("q")
            if q:
                qs = qs.filter(name__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = forms.PositionFilterForm(self.request.GET)
        return context


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
