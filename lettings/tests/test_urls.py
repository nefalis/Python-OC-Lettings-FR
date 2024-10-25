from django.test import TestCase
from django.urls import reverse


class LettingsURLsTests(TestCase):
    def test_index_url(self):
        """
        Test the index URL returns a 200 status code.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_non_existent_url(self):
        """
        Test that a non-existent URL returns a 404 status code.
        """
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)
