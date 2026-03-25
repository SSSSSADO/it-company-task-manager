from django.urls import path

from manager import views

app_name = "manager"

urlpatterns = [
    path("", views.index, name="index"),
    # Task paths
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    path(
        "tasks/<int:pk>",
        views.TaskDetailView.as_view(),
        name="task-detail"
    ),
    # Worker paths
    path("workers/", views.WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>",
        views.WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    # TaskType paths
    path(
        "task-types/",
        views.TaskTypeListView.as_view(),
        name="task-type-list"
    ),
    path(
        "task-types/<int:pk>",
        views.TaskTypeDetailView.as_view(),
        name="task-type-detail"
    ),
    # Position paths
    path(
        "positions/",
        views.PositionListView.as_view(),
        name="position-list"
    ),
]
