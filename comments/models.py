from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Represents a comment made by a user on a post.
    Attributes:
        owner (ForeignKey): The user who made the comment.
        post (ForeignKey): The post on which the comment is made.
        created (DateTimeField): The date and time of comment creation.
        body (TextField): The content of the comment.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=400)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Comment: {self.id}, for post: {self.post.id}"
