from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class IntegrationTests(TestCase):
    def test_profile_detail(self):
        """Test that a specific profile page loads successfully."""
        user = User.objects.create(username="testuser")
        Profile.objects.create(user=user, favorite_city="Paris")
        response = self.client.get(reverse("profiles:profile", kwargs={"username": "testuser"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paris")
