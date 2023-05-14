from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return obj.created.strftime("%dth %B %Y, %H:%M")

    class Meta:
        model = Post
        fields = ["id", "owner", "created", "body", "image"]
