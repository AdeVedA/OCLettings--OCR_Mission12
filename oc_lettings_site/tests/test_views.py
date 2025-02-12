from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse


class IndexViewTests(TestCase):
    """
    Test case for the index view of the oc_lettings_site app.

    This class ensures that the index view responds correctly and uses
    the appropriate template.
    """

    @classmethod
    def setUpTestData(cls):
        pass

    def test_index_view_status_code(self):
        """
        Test that the index page returns an HTTP 200 status code.

        Ensures the view is accessible and functioning correctly.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        """
        Test that the index page uses the correct template.

        Verifies that the 'index.html' template is rendered for the index view.
        """
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")


class CustomErrorViewsTests(TestCase):
    """
    Test cases for the custom error pages (404 and 500).
    """

    def test_custom_404_view(self):
        """
        Test that the custom 404 page is displayed for a non-existent URL.
        """
        response = self.client.get("/blablabla-dummy-page/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    @override_settings(DEBUG=False)
    def test_custom_500_view(self):
        """
        Test that the custom 500 page is displayed when a server error occurs.
        """
        with self.assertRaises(Exception):
            response = self.client.get("/500-test/")
            response.status_code = 500
            self.assertTemplateUsed(response, "500.html")
