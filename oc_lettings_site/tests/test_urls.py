from django.test import TestCase
from django.urls import resolve, reverse

from oc_lettings_site import views


class UrlsTests(TestCase):
    """
    Test case for verifying the URL patterns of the oc_lettings_site app.

    This class ensures that the URLs defined in the app are correctly mapped
    to their corresponding views.
    """

    @classmethod
    def setUpTestData(cls):
        pass

    def test_index_url_resolves(self):
        """
        Test that the URL for the index page resolves to the correct view.

        This test ensures that the 'index' URL name is mapped to the views.index function.
        """
        resolver = resolve(reverse("index"))
        self.assertEqual(resolver.func, views.index)
