from rest_framework import serializers
from .models import Post
from likes.models import Like


# class NullableImageField(serializers.ImageField):
#     """
#     Custom serializer field that allows a file upload or a null/empty value.
#     """

#     def to_internal_value(self, data):
#         if not data:
#             return None

#         return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model, providing a read-only 'owner' and
    'like_count' fields, custom 'created' and 'like_id' fields.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    created = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(source="owner.profile.avatar.url")
    comment_count = serializers.ReadOnlyField()

    # do something with this:
    image = serializers.ImageField(allow_null=True, required=False)

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
