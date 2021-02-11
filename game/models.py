from django.db import models
from django.contrib.auth.models import  User

from .mechmodels import *

# Create your models here.


class Enemy(models.Model):
    """An enemy that may be encountered while patrolling"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    max_hp = models.IntegerField(default=0)
    current_hp = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)
    armor = models.IntegerField(default=0)


    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class Event(models.Model):
    """An event that occurs while patrolling the outlands"""
    pass