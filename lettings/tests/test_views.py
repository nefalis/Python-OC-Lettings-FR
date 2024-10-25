from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingViewsTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Rue de la plaine',
            city='Ailleurs',
            state='IL',
            zip_code=61234,
            country_iso_code='FR'
        )
        self.letting = Letting.objects.create(
            title='Cozy Cottage',
            address=self.address
        )

    def test_index_view(self):
        """
        Test that the index view works correctly.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        """
        Test that the letting detail view works correctly for a specific letting.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.letting.address)

    def test_letting_detail_integration(self):
        """
        Integration test to verify the letting detail view.
        It checks the interaction between models, view, and template.
        """
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)

        # Vérifie le statut HTTP est correct
        self.assertEqual(response.status_code, 200)

        # Vérifie le bon template est utilisé
        self.assertTemplateUsed(response, 'lettings/letting.html')

        # Vérifie donnée du contexte
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.letting.address)

        # Vérifie certaines parties du contenu HTML
        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.letting.address.street)
        self.assertContains(response, self.letting.address.city)
