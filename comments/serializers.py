from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model, providing a read-only 'owner' field
    sourced from the username, and a custom string representation for the
    'created' field.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    # add user profile and avatar here once serializer is created
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return obj.created.strftime("%dth %B %Y, %H:%M")

    class Meta:
        model = Comment
        fields = ["id", "owner", "post", "created", "body"]
