from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import News, Announcement
from django.contrib.auth.models import User


# MODEL TESTS


class NewsModelTests(TestCase):
    def test_str_method(self):
        news = News.objects.create(
            title="Test News Item", body="Body", category="Other")
        expected_str = f"News 1 - Test News Item"
        self.assertEqual(str(news), expected_str)


class AnnouncementModelTests(TestCase):
    def test_str_method(self):
        announcement = Announcement.objects.create(body="Test announcement")
        expected_str = f"Announcement 1"
        self.assertEqual(str(announcement), expected_str)


# VIEW TESTS


class NewsFilterTests(TestCase):
    def setUp(self):
        News.objects.create(title="title", body="body", category="Other")
        News.objects.create(title="title", body="body", category="Anime")
        News.objects.create(title="title", body="body", category="TCG")
        News.objects.create(title="title", body="body", category="Games")

    def test_filter_off(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 4)

    def test_category_other(self):
        response = self.client.get("/news/?category=Other")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_category_anime(self):
        response = self.client.get("/news/?category=Anime")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_category_TCG(self):
        response = self.client.get("/news/?category=TCG")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_category_Games(self):
        response = self.client.get("/news/?category=Games")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_id_filter(self):
        response = self.client.get("/news/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["category"], "Other")


class NewsListTests(APITestCase):
    def setUp(self):
        News.objects.create(title="Test News Item",
                            body="Body", category="Other")

    def test_get_news_list(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_perform_create_without_user(self):
        response = self.client.post(
            "/news/", {"title": "title", "body": "body", "category": "Other"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(News.objects.count(), 1)

    def test_perform_create_with_user(self):
        User.objects.create_user(username="testuser", password="pass")
        self.client.login(username="testuser", password="pass")
        response = self.client.post(
            "/news/", {"title": "title", "body": "body", "category": "Other"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(News.objects.count(), 1)

    def test_perform_create_with_admin(self):
        admin = User.objects.create_user(username="admin", password="pass")
        admin.is_staff = True
        admin.save()
        self.client.login(username="admin", password="pass")
        response = self.client.post(
            "/news/", {"title": "title", "body": "body", "category": "Other"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 2)


class NewsDetailTests(APITestCase):
    def setUp(self):
        News.objects.create(title="Test News Item",
                            body="Body", category="Other")
        User.objects.create_user(username="testuser", password="pass")
        admin = User.objects.create_user(username="admin", password="pass")
        admin.is_staff = True
        admin.save()

    def test_invalid_news_id(self):
        response = self.client.get("/news/9999999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_news_id(self):
        response = self.client.get("/news/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_user_edit(self):
        response = self.client.patch("/news/1", {"body": "updated body"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cant_edit(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.patch("/news/1", {"body": "updated body"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_edit(self):
        self.client.login(username="admin", password="pass")
        response = self.client.put(
            "/news/1", {
                "title": "Test News Item",
                "body": "updated body",
                "category": "Other"
            })
        news = News.objects.filter(id=1).first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(news.body, "updated body")

    def test_no_user_cant_delete(self):
        response = self.client.delete("/news/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(News.objects.count(), 1)

    def test_user_cant_delete(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.delete("/news/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(News.objects.count(), 1)

    def test_admin_can_delete(self):
        self.client.login(username="admin", password="pass")
        response = self.client.delete("/news/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(News.objects.count(), 0)


class AnnouncementListTests(APITestCase):
    def setUp(self):
        Announcement.objects.create(body="Test announcement")

    def test_get_announcement_list(self):
        response = self.client.get("/announcements/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_perform_create_without_user(self):
        response = self.client.post(
            "/announcements/", {"body": "New announcement"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Announcement.objects.count(), 1)

    def test_perform_create_with_user(self):
        User.objects.create_user(username="testuser", password="pass")
        self.client.login(username="testuser", password="pass")
        response = self.client.post(
            "/announcements/", {"body": "new announcement"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Announcement.objects.count(), 1)

    def test_perform_create_with_admin(self):
        admin = User.objects.create_user(username="admin", password="pass")
        admin.is_staff = True
        admin.save()
        self.client.login(username="admin", password="pass")
        response = self.client.post(
            "/announcements/", {"body": "new announcement"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Announcement.objects.count(), 2)


class AnnouncementDetailTests(APITestCase):
    def setUp(self):
        Announcement.objects.create(body="Test announcement")
        admin = User.objects.create_user(username="admin", password="pass")
        admin.is_staff = True
        admin.save()
        User.objects.create_user(username="testuser", password="pass")

    def test_invalid_announcement_id(self):
        response = self.client.get("/announcements/99999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_announcement_id(self):
        response = self.client.get("/announcements/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_user_edit(self):
        response = self.client.patch(
            "/announcements/1", {"body": "updated announcements"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cant_edit(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.patch(
            "/announcements/1", {"body": "updated announcements"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_edit(self):
        self.client.login(username="admin", password="pass")
        response = self.client.patch(
            "/announcements/1", {"body": "updated announcement"})
        announcement = Announcement.objects.filter(id=1).first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(announcement.body, "updated announcement")

    def test_no_user_cant_delete(self):
        response = self.client.delete("/announcements/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Announcement.objects.count(), 1)

    def test_user_cant_delete(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.delete("/announcements/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Announcement.objects.count(), 1)

    def test_admin_can_delete(self):
        self.client.login(username="admin", password="pass")
        response = self.client.delete("/announcements/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Announcement.objects.count(), 0)
