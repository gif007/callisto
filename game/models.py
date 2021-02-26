from django.db import models
from django.contrib.auth.models import  User

from .mechmodels import *
from .eventmodels import *

# Create your models here.


class Enemy(models.Model):
    """An enemy that may be encountered while patrolling"""
    name = models.CharField(max_length=40, null=True)
    prefix = models.CharField(max_length=2, null=True, blank=True)
    desc = models.TextField(null=True)
    max_hp = models.IntegerField(default=0)
    current_hp = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)
    firerate = models.FloatField(default=1.0)
    armor = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    img = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


