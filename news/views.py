from rest_framework import generics
from pokebox.permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer, AnnouncementSerializer
from .models import News, Announcement


class NewsList(generics.ListCreateAPIView):
    """
    API view for listing and creating news items.
    """
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = News.objects.all().order_by("-created")


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
    queryset = Announcement.objects.all().order_by("-created")[:1]


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for showing a specific announcement and providing
    full permissions to admin users.
    """
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Announcement.objects.all().order_by("-created")
