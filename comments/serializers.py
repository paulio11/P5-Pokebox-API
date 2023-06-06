from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes Comment model instances to JSON format.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(
        source="owner.profile.avatar.url")
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        """
        Returns the formatted creation date of the comment.
        """
        return obj.created.strftime("%b %d %Y, %H:%M")

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
    Serializer for detailed Comment objects.
    Extends CommentSerializer to include additional details.
    """
    post = serializers.ReadOnlyField(source="post.id")
