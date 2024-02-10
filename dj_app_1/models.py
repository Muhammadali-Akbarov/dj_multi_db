"""
django models for psql
"""
from django.db import models


class Payment(models.Model):
    """
    tha pyment model that can be used for saving transactions
    """
    invoice = models.CharField(max_length=255)

    class Meta:
        """
        meta fields
        """
        db_table = "payment"
