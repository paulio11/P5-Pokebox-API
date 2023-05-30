from django.contrib.auth.models import User
from rest_framework import generics, permissions, filters
from pokebox.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    ).order_by("-created")
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["like_count", "comment_count", "created"]
    filterset_fields = ["owner__profile", "likes__owner__profile"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    ).order_by("-created")
