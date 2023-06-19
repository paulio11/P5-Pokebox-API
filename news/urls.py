from django.urls import path
from news import views


urlpatterns = [
    path("news/", views.NewsList.as_view()),
    path("news/<int:pk>", views.NewsDetail.as_view()),
    path("announcements/", views.AnnouncementList.as_view()),
    path("announcements/<int:pk>", views.AnnouncementDetail.as_view()),
]
