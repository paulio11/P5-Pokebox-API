from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current authenticated User, extending
    UserDetailsSerializer from dj_rest_auth. Includes additional fields from
    the user's profile (id, avatar, favorite pokemon).
    """

    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_avatar = serializers.ReadOnlyField(source="profile.avatar.url")
    profile_fav = serializers.ReadOnlyField(source="profile.favorite")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id",
            "profile_avatar",
            "profile_fav",
        )
