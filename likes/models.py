from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Represents a Like made by a User on a Post. Includes a creation timestamp.
    A unique constraint ensures a user can only like a particular post once.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # do I need related names?
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        unique_together = ["owner", "post"]

    def __str__(self):
        return f"{self.owner} - {self.post}"
