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
    path(
        "tasks/create/",
        views.TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
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
    path(
        "positions/<int:pk>",
        views.PositionDetailView.as_view(),
        name="position-detail"
    ),
    path(
        "positions/create/",
        views.PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/<int:pk>/update/",
        views.PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "positions/<int:pk>/delete/",
        views.PositionDeleteView.as_view(),
        name="position-delete"
    )
]
