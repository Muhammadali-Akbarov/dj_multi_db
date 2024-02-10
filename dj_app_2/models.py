"""
the database models that used with mysql
"""
from django.db import models


class Order(models.Model):
    """
    the orders model
    """
    status = models.BooleanField(default=False)

    class Meta:
        """
        meta fields
        """
        db_table = "order"
