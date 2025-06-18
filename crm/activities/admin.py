from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'customer', 'created_by', 'created_at')
    search_fields = ('description',)
    list_filter = ('activity_type', 'created_by')