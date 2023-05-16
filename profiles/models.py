from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django_resized import ResizedImageField


class Profile(models.Model):
    """
    Represents a user's profile. Includes information about the user, their
    favorite pokemon, a list of pokemon IDs, and an avatar. Profiles are
    ordered by creation date.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    about = models.TextField(
        max_length=400,
        default="Hello! I am a new trainer just starting my Pokémon adventure.",
        blank=True,
    )
    favorite = models.CharField(max_length=30, blank=True)
    pokemon = ArrayField(models.IntegerField(), default=list)
    avatar = ResizedImageField(
        upload_to="avatars/",
        size=[150, 150],
        crop=["middle", "center"],
        force_format="WEBP",
        default="../default-avatar_buqmfw",
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a new profile for each new user.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
