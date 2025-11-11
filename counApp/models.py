from django.db import models #(15)
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{7,15}$',
    message='Enter phone as digits, optional leading +, length 7-15.'
)

class ContactSubmission(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=16, validators=[phone_validator])
    address = models.CharField(max_length=250)
    message = models.TextField(max_length=500)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.username} — {self.email} ({self.submitted_at:%d-%m-%y %H:%M})"