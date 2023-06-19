from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    image = ResizedImageField(
        upload_to="news/",
        blank=True,
        null=True,
        size=[666, None],
        force_format="WEBP",
    )

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "News"

    def __str__(self):
        return f"News: {self.title}"


class Announcement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1000)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Announcement {self.id}"
