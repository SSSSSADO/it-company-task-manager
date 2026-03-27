from django import forms
from django.contrib.auth.forms import UserCreationForm

from manager.models import Position, Worker, TaskType, Task


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = ("username", "position", "first_name", "last_name", "email")


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("username", "position", "first_name", "last_name", "email")


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "description": forms.Textarea()
        }


class TaskFilterForm(forms.Form):
    q = forms.CharField(required=False, label="Search")  # поиск по имени
    is_completed = forms.ChoiceField(
        required=False,
        choices=[("", "All"), ("1", "Completed"), ("0", "Open")],
        label="Status"
    )
    priority = forms.ChoiceField(
        required=False,
        choices=[("", "All")] + list(Task.Priority.choices),
        label="Priority"
    )
    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        required=False,
        label="Task Type"
    )

class WorkerFilterForm(forms.Form):
    q = forms.CharField(required=False, label="Search")
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        required=False,
        label="Position"
    )


class TaskTypeFilterForm(forms.Form):
    q = forms.CharField(required=False, label="Search")


class PositionFilterForm(forms.Form):
    q = forms.CharField(required=False, label="Search")
