from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from .serializers import CommentSerializer
from .views import CommentList
from posts.models import Post


# VIEW TESTS


class CommentListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.post1 = Post.objects.create(owner=self.user, body="test post 1")
        post2 = Post.objects.create(owner=self.user, body="test post 2")
        comment = Comment.objects.create(
            owner=self.user, body="test comment for post 1", post=self.post1
        )
        comment2 = Comment.objects.create(
            owner=self.user, body="test comment for post 2", post=post2
        )

    def test_get_comment_list(self):
        response = self.client.get("/comments/")
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.data["count"], 2)

    def test_get_comment_list_for_post(self):
        response = self.client.get("/comments/?post=1")
        comments = Comment.objects.filter(post=self.post1)
        serializer = CommentSerializer(comments, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.data["count"], 1)

    def test_perform_create_without_user(self):
        response = self.client.post(
            "/comments/", {"post": self.post1.id, "body": "new comment"}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.count(), 2)

    def test_perform_create_with_user(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.post(
            "/comments/", {"post": self.post1.id, "body": "new comment"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 3)
        self.assertEqual(Comment.objects.last().owner, self.user)


class CommentDetailTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="pass")
        post = Post.objects.create(owner=user, body="test post")
        comment = Comment.objects.create(owner=user, post=post, body="test comment")
        user2 = User.objects.create_user(username="testuser2", password="pass")
        comment2 = Comment.objects.create(
            owner=user2, post=post, body="someone else's comment"
        )

    def test_invalid_comment_id(self):
        response = self.client.get("/comments/1000000")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_comment_id(self):
        response = self.client.get("/comments/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_edit_comment(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.put("/comments/1", {"body": "updated comment"})
        comment = Comment.objects.filter(id=1).first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(comment.body, "updated comment")

    def test_user_cant_edit_someone_elses_comment(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.put("/comments/2", {"body": "updated comment"})
        comment = Comment.objects.filter(id=2).first()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(comment.body, "updated comment")

    def test_logged_out_user_cant_edit(self):
        response = self.client.put("/comments/1", {"body": "updated comment"})
        comment = Comment.objects.filter(id=1).first()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(comment.body, "updated comment")

    def test_user_can_delete_comment(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.delete("/comments/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 1)

    def test_user_cant_delete_someone_elses_comment(self):
        self.client.login(username="testuser", password="pass")
        response = self.client.delete("/comments/2")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.count(), 2)

    def test_logged_out_user_cant_delete(self):
        response = self.client.delete("/comments/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.count(), 2)


# MODEL TESTS


class CommentModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.post = Post.objects.create(owner=self.user, body="test post")
        Comment.objects.create(owner=self.user, body="test comment", post=self.post)

    def test_str_method(self):
        comment = Comment.objects.filter(owner=self.user).first()
        expected_str = f"Comment: {comment.id}, for post: {self.post.id}"
        self.assertEqual(str(comment), expected_str)
