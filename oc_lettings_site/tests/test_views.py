from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):

    def test_index_view(self):
        """
        Test that the index view returns a 200 status code.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        """
        Test that the index view uses the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
