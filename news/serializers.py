from rest_framework import serializers
from .models import News, Announcement


class NewsSerializer(serializers.ModelSerializer):
    """
    Serializer for News objects.
    Serializes News model instances to JSON format.
    """
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        """
        Returns a custom string representation for the 'created' field.
        """
        return obj.created.strftime("%b %d %Y, %H:%M")

    class Meta:
        model = News
        fields = [
            "id", "body", "created"
        ]


class AnnouncementSerializer(serializers.ModelSerializer):
    """
    Serializer for Announcement objects.
    Serializes Announcement model instances to JSON format.
    """
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        """
        Returns a custom string representation for the 'created' field.
        """
        return obj.created.strftime("%b %d %Y, %H:%M")

    class Meta:
        model = Announcement
        fields = [
            "id", "body", "created", "read"
        ]
