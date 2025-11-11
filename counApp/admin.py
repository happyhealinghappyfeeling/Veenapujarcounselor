from django.contrib import admin #(15)
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'submitted_at')
    search_fields = ('username', 'email', 'phone', 'address', 'message')
    readonly_fields = ('submitted_at',)