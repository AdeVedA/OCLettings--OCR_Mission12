from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfileViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up the test datas for the profiles/view tests.
        """
        user1 = User.objects.create_user(username="testuser1", password="password123")
        user2 = User.objects.create_user(username="testuser2", password="password456")
        Profile.objects.create(user=user1, favorite_city="Paris")
        Profile.objects.create(user=user2, favorite_city="London")

    def test_profiles_index_view(self):
        """
        Test the profiles index view to verify it displays all profiles.
        """
        response = self.client.get(reverse("profiles:profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profiles_index.html")
        self.assertContains(response, "testuser1")
        self.assertContains(response, "testuser2")

    def test_profile_view(self):
        """
        Test the profile detail view for a specific user.
        """
        response = self.client.get(reverse("profiles:profile", args=["testuser1"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, "testuser1")
        self.assertContains(response, "Paris")

    def test_profile_view_404(self):
        """
        Test the profile view to verify it returns a 404 for a non-existent username.
        """
        url = reverse("profiles:profile", args=["nonexistentuser"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
