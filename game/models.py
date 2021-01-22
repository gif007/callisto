from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class MobileSuit(models.Model):
    controller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    helm = models.ForeignKey('Helm', on_delete=models.SET_NULL, null=True)
    chest = models.ForeignKey('Chest', on_delete=models.SET_NULL, null=True)
    left_arm = models.ForeignKey('LeftArm', on_delete=models.SET_NULL, null=True)
    right_arm = models.ForeignKey('RightArm', on_delete=models.SET_NULL, null=True)
    legs = models.ForeignKey('Legs', on_delete=models.SET_NULL, null=True)
    trinkets = models.ManyToManyField('Trinket')

    def __str__(self):
        return 'A mobile suit belonging to %s' % self.controller


class Helm(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    sight = models.IntegerField(default=0)


class Chest(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)


class LeftArm(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)


class RightArm(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)


class Legs(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)


class Trinket(models.Model):
    name = models.CharField(max_length=40, null=True)