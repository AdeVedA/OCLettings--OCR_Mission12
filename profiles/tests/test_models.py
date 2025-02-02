from django.contrib.auth.models import User
from django.test import TestCase

from profiles.models import Profile


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up data for the whole test class.
        """
        user = User.objects.create_user(username="testuser", password="passpassword")
        Profile.objects.create(user=user, favorite_city="Paris")

    def test_profile_str_representation(self):
        """
        Test the __str__ method of the Profile model to ensure it returns the username.
        """
        profile = Profile.objects.get(user__username="testuser")
        self.assertEqual(str(profile), "testuser")
