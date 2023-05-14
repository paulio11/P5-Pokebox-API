from django.contrib.auth.models import User
from rest_framework import generics, permissions
from pokebox.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count


class PostList(generics.ListCreateAPIView):
    """
    A view that provides the list of Posts and allows authenticated users to
    create new Posts. Query can be filtered by 'owner' and is annotated with a
    count of distinct likes.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Returns a queryset that includes a count of distinct likes and can be
        filtered by 'owner'.
        """
        queryset = Post.objects.annotate(
            like_count=Count("likes", distinct=True),
        ).order_by("-created")
        username = self.request.query_params.get("owner", None)
        if username is not None:
            owner = get_object_or_404(User, username=username)
            queryset = queryset.filter(owner=owner)
        return queryset

    def perform_create(self, serializer):
        """
        Sets the owner of a new Post to the authenticated user making the
        request.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view that provides detail of a Post. Only the owner can update or delete
    the Post. The query is annotated with a count of distinct likes.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        like_count=Count("likes", distinct=True),
    ).order_by("-created")
