from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTests(TestCase):

    def setUp(self):
        """
        Setup method to create a User and a Profile for testing.
        """
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')


    def test_profile_creation(self):
        """
        Test the Profile model is correctly created.
        """
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.favorite_city, 'Paris')
        self.assertEqual(profile.user.username, 'testuser')


    def test_profile_favorite_city(self):
        """
        Test that the favorite_city field can be blank.
        """
        self.profile.favorite_city = ''
        self.profile.save()
        self.assertEqual(self.profile.favorite_city, '')
