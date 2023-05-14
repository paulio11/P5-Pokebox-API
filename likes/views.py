from .models import Like
from .serializers import LikeSerializer
from rest_framework import generics, permissions
from pokebox.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    A view that provides the list of Likes and allows authenticated users to
    create new Likes.
    """

    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        Sets the owner of a new Like to the authenticated user making the
        request.
        """
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    A view that provides detail of a Like. Only the owner can delete the Like.
    """

    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
