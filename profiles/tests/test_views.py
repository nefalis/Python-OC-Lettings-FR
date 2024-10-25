from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesViewsTest(TestCase):

    def setUp(self):
        """
        Set up test data by creating users and profiles.
        """
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.profile1 = Profile.objects.create(user=self.user1, favorite_city='Paris')
        self.profile2 = Profile.objects.create(user=self.user2, favorite_city='London')

    def test_index_view(self):
        """
        Test that the index view works correctly.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

        profiles_list = response.context['profiles_list']
        self.assertIn(self.profile1, profiles_list)
        self.assertIn(self.profile2, profiles_list)

    def test_index_view_no_profiles(self):
        """
        Test the index view when there are no profiles in the database.
        """
        Profile.objects.all().delete()
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

        # Verify that the profiles list is empty
        profiles_list = response.context['profiles_list']
        self.assertEqual(len(profiles_list), 0)

    def test_profile_view(self):
        """
        Test that the profile view works correctly for a given user.
        """
        response = self.client.get(reverse('profiles:profile', args=['user1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

        # Vérifie que les données de profil sont dans le contexte
        self.assertEqual(response.context['profile'].user.username, 'user1')
        self.assertEqual(response.context['profile'].favorite_city, 'Paris')

    def test_profile_detail_integration(self):
        """
        Integration test for the profile view.
        It verifies the interaction between models, view, and template.
        """
        url = reverse('profiles:profile', args=['user1'])
        response = self.client.get(url)

        # Vérifie le statut HTTP est correct
        self.assertEqual(response.status_code, 200)

        # Vérifie que le bon template est utilisé
        self.assertTemplateUsed(response, 'profiles/profile.html')

        # Vérifie les données du contexte
        self.assertEqual(response.context['profile'].user.username, 'user1')
        self.assertEqual(response.context['profile'].favorite_city, 'Paris')

        # Vérifie certaines parties du contenu HTML
        self.assertContains(response, 'user1')
        self.assertContains(response, 'Paris')
