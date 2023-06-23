from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current authenticated User, extending
    UserDetailsSerializer from dj_rest_auth. Includes id and
    avatar field from the user's profile, and if they are staff.
    """

    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_avatar = serializers.ReadOnlyField(source="profile.avatar.url")
    is_staff = serializers.SerializerMethodField()

    def get_is_staff(self, obj):
        return obj.is_staff

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ("profile_id", "profile_avatar", "is_staff")
