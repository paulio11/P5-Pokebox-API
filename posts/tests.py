from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer
from likes.models import Like
from .views import PostFilter


# VIEW TESTS


class PostListTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        post = Post.objects.create(owner=user, body="test post")

    def test_get_post_list(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_perform_create_without_user(self):
        response = self.client.post("/posts/", {"body": "new post"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 1)

    def test_perform_create_with_user(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.post("/posts/", {"body": "new post"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)


class PostDetailTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        Post.objects.create(owner=user, body="test post")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        Post.objects.create(owner=user2, body="test post 2")

    def test_invalid_post_id(self):
        response = self.client.get("/posts/100000")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_post_id(self):
        response = self.client.get("/posts/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_edit_post(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.put("/posts/1", {"body": "updated post"})
        post = Post.objects.filter(id=1).first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.body, "updated post")

    def test_user_cant_edit_someone_elses_post(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.put("/posts/2", {"body": "updated post"})
        post = Post.objects.filter(id=2).first()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(post.body, "updated post")

    def test_logged_out_user_cant_edit(self):
        response = self.client.put("/posts/2", {"body": "updated post"})
        post = Post.objects.filter(id=2).first()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(post.body, "updated post")

    def test_user_can_delete_post(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.delete("/posts/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)

    def test_user_cant_delete_someone_elses_post(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.delete("/posts/2")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 2)

    def test_logged_out_user_cant_delete(self):
        response = self.client.delete("/posts/2")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 2)


class PostFilterTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        self.post1 = Post.objects.create(
            owner=user, body="test post with image", image="test.jpg"
        )
        self.post2 = Post.objects.create(
            owner=user2, body="test post user 1 liked")
        Like.objects.create(owner=user, post=self.post2)

    def test_filter_off(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_filter_has_image(self):
        response = self.client.get("/posts/", {"has_image": "true"})
        results = response.data.get("results", [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(results[0]["body"], "test post with image")

    def test_filter_owner(self):
        response = self.client.get("/posts/", {"owner__profile": "1"})
        results = response.data.get("results", [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(results[0]["owner"], "testuser")

    def test_liked_filter(self):
        response = self.client.get("/posts/", {"likes__owner__profile": "1"})
        results = response.data.get("results", [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(results[0]["body"], "test post user 1 liked")

    def test_filter_returned_queryset_if_value_is_true(self):
        queryset = Post.objects.all()
        filter = PostFilter()
        filtered_queryset = filter.filter_has_image(
            queryset, "has_image", True)
        self.assertEqual(len(filtered_queryset), 1)
        self.assertTrue(self.post1 in filtered_queryset)
        self.assertFalse(self.post2 in filtered_queryset)

    def test_filter_returned_queryset_if_value_is_false(self):
        queryset = Post.objects.all()
        filter = PostFilter()
        filtered_queryset = filter.filter_has_image(
            queryset, "has_image", False)
        self.assertEqual(len(filtered_queryset), 2)
        self.assertTrue(self.post1 in filtered_queryset)
        self.assertTrue(self.post2 in filtered_queryset)


# MODEL TESTS


class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="pass")
        Post.objects.create(owner=self.user, body="test post")

    def test_str_method(self):
        post = Post.objects.filter(owner=self.user).first()
        expected_str = f"Post: {post.id}, by {self.user}"
        self.assertEqual(str(post), expected_str)


# SERIALIZER TESTS


class PostSerializerTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        post = Post.objects.create(owner=user, body="test post")
        post2 = Post.objects.create(owner=user2, body="test post 2")
        self.like = Like.objects.create(owner=user2, post=post)

    def test_get_like_id(self):
        self.client.login(username="testuser2", password="pass")
        response = self.client.get("/posts/1")
        self.assertEqual(response.data["like_id"], self.like.id)

    def test_get_like_id_when_none(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.get("/posts/2")
        self.assertIsNone(response.data["like_id"])
