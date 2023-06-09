from django.contrib.auth.models import User
from rest_framework import generics, permissions, filters
from pokebox.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend


class PostFilter(rest_framework.FilterSet):
    """
    Provides filtering options for post instances
    """
    has_image = rest_framework.BooleanFilter(
        field_name="image", method="filter_has_image"
    )

    def filter_has_image(self, queryset, name, value):
        """
        Filter method for filtering posts based on the presence of an image.
        """
        if value:
            return queryset.exclude(image="")
        return queryset

    class Meta:
        model = Post
        fields = {
            "owner__profile": ["exact"],
            "likes__owner__profile": ["exact"],
        }


class PostList(generics.ListCreateAPIView):
    """
    API view for listing and creating posts
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    ).order_by("-created")
    filter_backends = [
        filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter
    ]
    ordering_fields = ["like_count", "comment_count", "created"]
    filterset_class = PostFilter
    search_fields = ["owner__username", "body"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for showing a specific post and providing
    full permissions to the post owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    ).order_by("-created")
