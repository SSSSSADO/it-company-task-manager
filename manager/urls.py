from django.urls import path

from manager import views

app_name = "manager"

urlpatterns = [
    path("", views.index, name="index"),
    # Task paths
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    # Worker paths
    path("workers/", views.WorkerListView.as_view(), name="worker-list"),
    # TaskType paths
    path(
        "task-types/",
        views.TaskTypeListView.as_view(),
        name="task-type-list"
    ),
    # Position paths
    path(
        "positions/",
        views.PositionListView.as_view(),
        name="position-list"
    ),
]
