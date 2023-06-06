from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from posts.models import Post
from .models import Like


# VIEW TESTS


class LikeListTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        self.post = Post.objects.create(owner=user, body="test post")
        self.post2 = Post.objects.create(owner=user2, body="test post 2")
        Like.objects.create(owner=user2, post=self.post)

    def test_get_like_list(self):
        response = self.client.get("/likes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_perform_create_without_user(self):
        response = self.client.post("/likes/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Like.objects.count(), 1)

    def test_perform_create_with_user(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.post("/likes/", {"post": self.post2.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 2)


class LikeDetailTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        post = Post.objects.create(owner=user, body="test post")
        post2 = Post.objects.create(owner=user, body="test post 2")
        Like.objects.create(owner=user2, post=post)
        Like.objects.create(owner=user, post=post2)

    def test_invalid_like_id(self):
        response = self.client.get("/likes/1000000")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_like_id(self):
        response = self.client.get("/likes/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_like(self):
        self.client.login(username="testuser2", password="pass")
        response = self.client.delete("/likes/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Like.objects.count(), 1)

    def test_user_cant_delete_someone_elses_like(self):
        self.client.login(username="testuser2", password="pass")
        response = self.client.delete("/likes/2")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Like.objects.count(), 2)

    def test_logged_out_user_cant_delete_like(self):
        response = self.client.delete("/likes/2")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Like.objects.count(), 2)


# MODEL TESTS


class LikeModelTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        self.user2 = User.objects.create_user(username="testuser2", password="pass")
        self.post = Post.objects.create(owner=user, body="test post")
        Like.objects.create(owner=self.user2, post=self.post)

    def test_str_method(self):
        like = Like.objects.filter(owner=self.user2).first()
        expected_str = f"{self.user2} - {self.post}"
        self.assertEqual(str(like), expected_str)


# SERIALIZER TESTS


class LikeSerializerTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        self.post = Post.objects.create(owner=user, body="test post")
        Like.objects.create(owner=user2, post=self.post)

    def test_create_duplicate_like(self):
        self.client.login(username="testuser2", password="pass")
        response = self.client.post("/likes/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["detail"], "Duplicate like. You have already liked this post."
        )
