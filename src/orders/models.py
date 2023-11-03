from django.db import models
from django.contrib.postgres.fields import ArrayField

from accounts.models import User


class Orders(models.Model):
    ORDER_STATE = [
        ('NW', 'New'),
        ('REG', 'Registered'),
        ('APPR', 'Approved'),
        ('SNT', 'Sent'),
        ('DLV', 'Delivered'),
        ('PD', 'Paid'),
        ('CNL', 'Canceled')
    ]

    state = models.CharField(choices=ORDER_STATE, default='NW')
    client = models.ForeignKey(User, on_delete=models.SET_NULL)
    grant_date = models.DateField(null=True)
    order_history = models.OneToOneField(to="States", on_delete=models.SET_NULL)


class States(models.Model):
    states = ArrayField(
        models.CharField(max_length=20),
        blank=True
    )
