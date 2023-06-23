from rest_framework.test import APITestCase
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializers import CurrentUserSerializer


# VIEW TESTS


class RootRouteTest(APITestCase):
    def test_root_route(self):
        response = self.client.get("/")

        # Assert response status code
        self.assertEqual(response.status_code, 200)

        # Assert message
        self.assertEqual(
            response.data, {"message": "This is the backend API for Pokébox!"}
        )


class LogoutRouteTest(APITestCase):
    def test_logout_root(self):
        response = self.client.post("/dj-rest-auth/logout")

        # Assert response status code
        self.assertEqual(response.status_code, 200)

        # Assert cookies are cleared
        self.assertEqual(response.cookies["p5-pokebox-auth"].value, "")
        self.assertEqual(
            response.cookies["p5-pokebox-refresh-token"].value, "")

        # Assert cookie attributes
        self.assertTrue(response.cookies["p5-pokebox-auth"]["httponly"])
        self.assertEqual(
            response.cookies["p5-pokebox-auth"]["expires"],
            "Thu 01 Jan 1970 00:00:00 GMT",
        )
        self.assertEqual(response.cookies["p5-pokebox-auth"]["max-age"], 0)
        self.assertEqual(
            response.cookies["p5-pokebox-auth"]["samesite"], "None")
        self.assertTrue(response.cookies["p5-pokebox-auth"]["secure"])

        self.assertTrue(
            response.cookies["p5-pokebox-refresh-token"]["httponly"])
        self.assertEqual(
            response.cookies["p5-pokebox-refresh-token"]["expires"],
            "Thu 01 Jan 1970 00:00:00 GMT",
        )
        self.assertEqual(
            response.cookies["p5-pokebox-refresh-token"]["max-age"], 0)
        self.assertEqual(
            response.cookies["p5-pokebox-refresh-token"]["samesite"], "None"
        )
        self.assertTrue(response.cookies["p5-pokebox-refresh-token"]["secure"])


# SERIALIZER TESTS

class UserSerializerTests(TestCase):
    def test_user_is_not_staff(self):
        user = User.objects.create_user(
            username="testuser", password="pass", is_staff=False)
        serializer = CurrentUserSerializer(user)
        serialized_data = serializer.data
        is_staff = serialized_data["is_staff"]
        self.assertFalse(is_staff)

    def test_admin_is_staff(self):
        admin = User.objects.create_user(
            username="admin", password="pass", is_staff=True)
        serializer = CurrentUserSerializer(admin)
        serialized_data = serializer.data
        is_staff = serialized_data["is_staff"]
        self.assertTrue(is_staff)
