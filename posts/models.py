from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Post(models.Model):
    """
    Represents a Post created by a User. Includes a creation timestamp, text
    body, and optional image. Posts are ordered by creation date.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=400)
    image = ResizedImageField(
        upload_to="images/",
        blank=True,
        null=True,
        size=[600, None],
        force_format="WEBP",
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Post: {self.id}, by {self.owner}"
