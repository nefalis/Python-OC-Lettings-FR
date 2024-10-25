from django.test import TestCase
from lettings.models import Address, Letting
from django.core.exceptions import ValidationError


class AddressModelTest(TestCase):

    def setUp(self):
        """
        Set up an Address instance to use in tests
        """
        self.address = Address.objects.create(
            number=123,
            street='Rue de la plaine',
            city='Ailleurs',
            state='IL',
            zip_code=61234,
            country_iso_code='FR'
        )

    def test_address_creation(self):
        """
        Test that an Address instance is created correctly.
        """
        address = Address.objects.get(id=self.address.id)
        self.assertEqual(str(address), '123 Rue de la plaine')
        self.assertEqual(address.city, 'Ailleurs')

    def test_invalid_number(self):
        """
        Test that an Address with an invalid number (too large) raises a ValidationError.
        """
        address = Address(
            number=10000,
            street='Rue de la plaine',
            city='Ailleurs',
            state='IL',
            zip_code=61234,
            country_iso_code='FR'
        )
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_invalid_state_length(self):
        """
        Test that the state field requires exactly 2 characters.
        """
        address = Address(
            number=123,
            street='Rue de la plaine',
            city='Ailleurs',
            state='I',
            zip_code=61234,
            country_iso_code='FR'
        )
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_invalid_country_code(self):
        """
        Test that the country_iso_code field requires exactly 3 characters.
        """
        address = Address(
            number=123,
            street='Rue de la plaine',
            city='Ailleurs',
            state='IL',
            zip_code=61234,
            country_iso_code='F'
        )
        with self.assertRaises(ValidationError):
            address.full_clean()


class LettingModelTest(TestCase):

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

    def test_letting_creation(self):
        """
        Test that a Letting instance is created correctly.
        """
        letting = Letting.objects.get(id=self.letting.id)
        self.assertEqual(str(letting), 'Cozy Cottage')
        self.assertEqual(letting.address, self.address)

    def test_letting_invalid_title(self):
        """
        Test that creating a Letting with an invalid title.
        """
        with self.assertRaises(ValidationError):
            invalid_letting = Letting(title='', address=self.address)
            invalid_letting.full_clean()
            invalid_letting.save()
