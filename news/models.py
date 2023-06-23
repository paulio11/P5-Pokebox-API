from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class News(models.Model):
    """
    Represents a news article. Includes creation date, a title, body
    (the article) text, an optional image, and category chosen from a list.
    Ordered by creation date.
    """

    CATEGORIES = (
        ("Games", "Games"),
        ("Anime", "Anime"),
        ("TCG", "TCG"),
        ("Other", "Other"),
    )

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
    category = models.CharField(max_length=5, choices=CATEGORIES)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "News"

    def __str__(self):
        return f"News {self.id} - {self.title}"


class Announcement(models.Model):
    """
    Represents an announcement, a simple model including only creation date
    and body (the announcement) text. Ordered by creation date.
    """
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1000)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Announcement {self.id}"
