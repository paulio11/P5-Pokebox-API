from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model, providing a read-only 'owner' field
    sourced from the username, and a custom string representation for the
    'created' field.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(source="owner.profile.avatar.url")
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return obj.created.strftime("%dth %B %Y, %H:%M")

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "post",
            "created",
            "body",
            "profile_id",
            "profile_avatar",
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for a detailed view of a Comment, extending CommentSerializer
    and adding a read-only 'post' field sourced from the post's ID.
    """

    post = serializers.ReadOnlyField(source="post.id")
