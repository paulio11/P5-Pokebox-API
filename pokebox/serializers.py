from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current authenticated User, extending
    UserDetailsSerializer from dj_rest_auth. Includes id field from
    the user's profile.
    """

    profile_id = serializers.ReadOnlyField(source="profile.id")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("profile_id",)
