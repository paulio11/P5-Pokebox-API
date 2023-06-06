from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from pokebox.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from django.db.models import F, Func, ExpressionWrapper, IntegerField


class ProfileList(generics.ListAPIView):
    """
    API view for listing profiles.
    Can be ordered by owner, col_size, and created.
    Can be filtered by owner.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        col_size=ExpressionWrapper(
            Func(
                F("pokemon"),
                function="array_length",
                template="%(function)s(%(expressions)s, 1)",
            ),
            output_field=IntegerField(),
        )
    ).order_by("-created")
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["owner__username", "col_size", "created"]
    filterset_fields = ["owner__username"]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    API view for a single detailed profile
    Provides full permission to owners of the profile.
    """
    queryset = Profile.objects.annotate(
        col_size=ExpressionWrapper(
            Func(
                F("pokemon"),
                function="array_length",
                template="%(function)s(%(expressions)s, 1)",
            ),
            output_field=IntegerField(),
        )
    )
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
