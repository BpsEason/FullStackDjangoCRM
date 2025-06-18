from django.test import TestCase
from django.contrib.auth.models import User
from customers.models import Customer
from .models import Activity

class ActivityModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com',
            created_by=self.user
        )
        self.activity = Activity.objects.create(
            activity_type='CALL',
            customer=self.customer,
            description='Test call',
            created_by=self.user
        )

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'CALL - Test Customer')