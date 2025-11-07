# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal

# Create your models here

class CustomUser(AbstractUser):
    # keep username field (simpler). If you prefer email-only login later, we can switch USERNAME_FIELD.
    email = models.EmailField(unique=True)  # optional but recommended
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    is_kyc_verified = models.BooleanField(default=False)
    wallet_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username or self.email
