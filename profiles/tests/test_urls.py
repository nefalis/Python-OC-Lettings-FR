from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles import views


class ProfilesUrlsTests(SimpleTestCase):

    def test_index_url(self):
        """
        Test that the index URL resolves to the correct view.
        """
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_profile_url(self):
        """
        Test that the profile URL resolves to the correct view.
        """
        # On vérifie si l'URL pour un nom d'utilisateur se résout correctement
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(resolve(url).func, views.profile)
