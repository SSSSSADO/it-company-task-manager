from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from manager.models import Worker, Position, Task, TaskType


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "position",
        "first_name",
        "last_name",
        "email"
    )
    search_fields = ("username", "email")
    list_filter = ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "is_completed", "priority", "deadline",)
    search_fields = ("name",)
    list_filter = ("priority", "is_completed", "task_type")
