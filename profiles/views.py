from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from pokebox.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    A view that provides the list of Profiles with optional sorting.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Optionally sorts the Profiles based on the parameters in the request.
        """
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get("sort_by", "owner")
        sort_order = self.request.query_params.get("sort_order", "asc")

        if sort_by == "pokemon":
            sort_by = "pokemon__len"

        if sort_by == "owner":
            sort_by = "owner__username"

        if sort_order == "desc":
            sort_by = "-" + sort_by

        return queryset.order_by(sort_by)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    A view that provides detail of a Profile. Only the owner can update the
    Profile.
    """

    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
