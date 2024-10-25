from django.test import TestCase
from django.urls import reverse, resolve
from oc_lettings_site import views


class UrlsTests(TestCase):

    def test_index_url(self):
        """
        Test that the index URL resolves to the correct view.
        """
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_lettings_url(self):
        """
        Test that the lettings URL includes the correct app's URLs.
        """
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profiles_url(self):
        """
        Test that the profiles URL includes the correct app's URLs.
        """
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
