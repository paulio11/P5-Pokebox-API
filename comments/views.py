from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListAPIView):
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
        querset = Comment.objects.all()
        post = self.request.query_params.get("post", None)
        if post is not None:
            post = get_object_or_404(Post, id=post)
            queryset = querset.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        """
        Sets the owner of a new Comment to the authenticated user making the
        request.
        """
        serializer.save(owner=self.request.user)
