from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer

class Activity(models.Model):
    ACTIVITY_TYPES = (
        ('CALL', 'Call'),
        ('MEETING', 'Meeting'),
        ('TASK', 'Task'),
    )
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity_type} - {self.customer.name}"