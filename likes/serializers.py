from rest_framework import serializers
from django.db import IntegrityError
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model, providing a read-only 'owner' field sourced
    from the username. Overrides the create method to handle possible
    duplicate Likes.
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Like
        fields = ["id", "owner", "post", "created"]

    def create(self, validated_data):
        """
        Tries to create a new Like instance and handles IntegrityError if a
        duplicate is found.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
