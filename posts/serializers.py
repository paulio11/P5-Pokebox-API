from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post objects.
    Serializes Post model instances to JSON format.
    Provides addtional fields for profile information,
    and counts for likes and comments.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    created = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(
        source="owner.profile.avatar.url")
    comment_count = serializers.ReadOnlyField()

    def get_like_id(self, obj):
        """
        Returns the ID of the Like object for the Post if the authenticated
        user has liked the post.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_created(self, obj):
        """
        Returns a custom string representation for the 'created' field.
        """
        return obj.created.strftime("%b %d %Y, %H:%M")

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "created",
            "body",
            "image",
            "like_id",
            "like_count",
            "profile_id",
            "profile_avatar",
            "comment_count",
        ]
