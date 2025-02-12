from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class IntegrationTests(TestCase):
    def test_letting_detail(self):
        """Test that a specific letting page loads successfully."""
        address = Address.objects.create(
            number=123,
            street="Avenue Jean Jaures",
            city="Paris",
            state="Paris 19è",
            zip_code=75020,
            country_iso_code="France",
        )
        letting = Letting.objects.create(title="Cozy Apartment", address=address)
        response = self.client.get(reverse("lettings:letting", kwargs={"letting_id": letting.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Apartment")
