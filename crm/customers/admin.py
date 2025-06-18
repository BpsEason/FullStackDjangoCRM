from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_by', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_by',)