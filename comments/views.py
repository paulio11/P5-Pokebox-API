from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from pokebox.permissions import IsOwnerOrReadOnly
from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    A view that provides the list of Comments and allows authenticated users
    to create new Comments.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally filters the Comments based on the 'post' parameter in the
        request.
        """
        queryset = Comment.objects.all()
        post = self.request.query_params.get("post", None)
        if post is not None:
            post = get_object_or_404(Post, id=post)
            queryset = queryset.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        """
        Sets the owner of a new Comment to the authenticated user making the
        request.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view that provides detail of a Comment. Only the owner can update or
    delete the Comment.
    """

    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
