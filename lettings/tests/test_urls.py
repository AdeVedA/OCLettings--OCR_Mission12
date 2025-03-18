from django.test import SimpleTestCase
from django.urls import resolve, reverse

from lettings import views


class LettingsURLsTest(SimpleTestCase):
    """
    Test case for verifying the URL patterns of the lettings app.

    This class checks if the URLs defined in the lettings app are correctly mapped
    to their respective views.
    """

    def test_lettings_index_url(self):
        """
        Test if the lettings index URL properly resolves to lettings_index view.
        """
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_url(self):
        """
        Test if the letting detail URL properly resolves to letting view.
        """
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, views.letting)
