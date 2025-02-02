from django.test import TestCase

from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    """
    Test case for the Address model.

    This class verifies that the string representation of the Address model
    is correctly formatted.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for Address model.

        Creates a sample Address instance to be used in the tests.
        """
        cls.address = Address.objects.create(
            number=123,
            street="Rue des fleurs",
            city="PARIS",
            state="IDF",
            zip_code=75018,
            country_iso_code="FR",
        )

    def test_address_str(self):
        """
        Test the string representation of the Address model.

        Ensures that the __str__ method returns the correct format.
        """
        self.assertEqual(str(self.address), "123 Rue des fleurs")


class LettingModelTest(TestCase):
    """
    Test case for the Letting model.

    This class verifies that the string representation of the Letting model
    is correctly formatted.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for Letting model.

        Creates a sample Address and Letting instance to be used in the tests.
        """
        cls.address = Address.objects.create(
            number=321,
            street="Rue infinie",
            city="Panam",
            state="IDF",
            zip_code=75000,
            country_iso_code="FR",
        )
        cls.letting = Letting.objects.create(title="Appart mignon", address=cls.address)

    def test_letting_str(self):
        """
        Test the string representation of the Letting model.

        Ensures that the __str__ method returns the correct title.
        """
        self.assertEqual(str(self.letting), "Appart mignon")
