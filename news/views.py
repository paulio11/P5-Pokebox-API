from rest_framework import generics, filters
from pokebox.permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer, AnnouncementSerializer
from .models import News, Announcement
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend


class NewsFilter(rest_framework.FilterSet):
    category = rest_framework.MultipleChoiceFilter(
        field_name="category",
        choices=News.CATEGORIES,
        conjoined=True
    )

    class Meta:
        model = News
        fields = ['category']


class NewsList(generics.ListCreateAPIView):
    """
    API view for listing and creating news items.
    """
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = News.objects.all().order_by("-created")
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = NewsFilter
    search_fields = ["title", "body"]


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for showing a specific news item and providing
    full permissions to admin users.
    """
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = News.objects.all().order_by("-created")


class AnnouncementList(generics.ListCreateAPIView):
    """
    API view for listing and creating announcements.
    """
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Announcement.objects.all().order_by("-created")


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for showing a specific announcement and providing
    full permissions to admin users.
    """
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Announcement.objects.all().order_by("-created")
