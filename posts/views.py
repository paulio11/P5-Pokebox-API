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
    has_image = rest_framework.BooleanFilter(
        field_name="image", method="filter_has_image"
    )

    def filter_has_image(self, queryset, name, value):
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
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    ).order_by("-created")
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["like_count", "comment_count", "created"]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    ).order_by("-created")
