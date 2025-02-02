from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Model representing an address.

    Attributes:
        number (PositiveIntegerField): The house or building number (maximum 4 digits).
        street (CharField): The name of the street (maximum 64 characters).
        city (CharField): The city name (maximum 64 characters).
        state (CharField): The state code (2 characters).
        zip_code (PositiveIntegerField): The ZIP code (maximum 5 digits).
        country_iso_code (CharField): The ISO country code (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns the string representation of the address.

        Returns:
            str: A string in the format "<number> <street>".
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Model representing a letting.

    Attributes:
        title (CharField): The title of the letting (maximum 256 characters).
        address (OneToOneField): A one-to-one relationship to the Address model.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
