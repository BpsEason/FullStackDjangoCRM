from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer

class CustomerModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com',
            phone='1234567890',
            address='Test Address',
            created_by=self.user
        )

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Test Customer')