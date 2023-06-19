from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1000)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "News"

    def __str__(self):
        return f"News {self.id}"


class Announcement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1000)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Announcement {self.id}"
