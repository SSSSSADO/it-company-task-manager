from django.urls import path

from manager import views

app_name = "manager"

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
]
