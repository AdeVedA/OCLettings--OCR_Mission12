from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Represents a user profile linked to a Django User model.

    Attributes:
        user (User): A one-to-one relationship with the User model.
        favorite_city (str): The user's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the string representation of the Profile, which is the username.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
