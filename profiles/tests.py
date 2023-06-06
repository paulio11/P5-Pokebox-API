from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase


# VIEW TESTS


class ProfileListTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="red", password="pass")
        User.objects.create_user(username="blue", password="pass")

    def test_profile_creation(self):
        response = self.client.get("/profiles/")
        count = Profile.objects.count()
        self.assertEqual(count, 2)

    def test_profile_list(self):
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="red", password="pass")
        User.objects.create_user(username="blue", password="pass")

    def test_invalid_profile_id(self):
        response = self.client.get("/profiles/10000000")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_profile_id(self):
        response = self.client.get("/profiles/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_profile(self):
        self.client.login(username="red", password="pass")
        response = self.client.put("/profiles/1", {"about": "hello"})
        profile = Profile.objects.filter(owner=1).first()
        self.assertEqual(profile.about, "hello")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_profile(self):
        self.client.login(username="red", password="pass")
        response = self.client.put("/profiles/2", {"about": "banana"})
        profile = Profile.objects.filter(owner=2).first()
        self.assertNotEqual(profile.about, "banana")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# MODEL TESTS


class ProfileModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="pass")

    def test_str_method(self):
        profile = Profile.objects.filter(owner=self.user).first()
        expected_str = f"{self.user}'s profile"
        self.assertEqual(str(profile), expected_str)
