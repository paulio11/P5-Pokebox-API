from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Represents a Comment made by a User on a Post. Includes a creation
    timestamp and a text body. Comments are ordered by creation date.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=400)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Comment: {self.id}, for post: {self.post.id}"
