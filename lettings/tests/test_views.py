from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsViewsTest(TestCase):
    """
    Test case for verifying the views of the lettings app.

    This class checks the response status, templates used, and context data
    returned by the lettings views.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the entire TestCase.

        This method creates an Address and Letting instance to be used
        for all test methods.
        """
        cls.address = Address.objects.create(
            number=10,
            street="square du bourbonnais",
            city="Montigny",
            state="IDF",
            zip_code=78180,
            country_iso_code="FR",
        )
        cls.letting = Letting.objects.create(title="Villa du SAN", address=cls.address)

    def test_lettings_index_view(self):
        """
        Test if the lettings index view returns a 200 status code,
        uses the correct template, and contains the expected context data.
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertIn("lettings_list", response.context)

    def test_letting_view(self):
        """
        Test if the letting detail view returns a 200 status code,
        uses the correct template, and contains the expected context data.
        """
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertEqual(response.context["title"], "Villa du SAN")
        self.assertEqual(response.context["address"], self.address)
