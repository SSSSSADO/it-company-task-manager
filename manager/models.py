from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("manager:position_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workers"
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def get_absolute_url(self):
        return reverse("manager:worker_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return (
            f"{self.username} ({self.position})" if self.position
            else f"{self.username} (Not Defined)"
        )


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("manager:task_type_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        URGENT = "URGENT", "Urgent"

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks"
    )

    class Meta:
        ordering = ["-deadline"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def get_absolute_url(self):
        return reverse("manager:task_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return (
            f"{self.name} ({'Done' if self.is_completed else 'In progress'})"
        )
