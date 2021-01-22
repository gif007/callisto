from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class MobileSuit(models.Model):
    """An object representing a mobile suit fitted with equipment"""
    controller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    helm = models.ForeignKey('Helm', on_delete=models.SET_NULL, null=True, blank=True)
    chest = models.ForeignKey('Chest', on_delete=models.SET_NULL, null=True, blank=True)
    left_arm = models.ForeignKey('LeftArm', on_delete=models.SET_NULL, null=True, blank=True)
    right_arm = models.ForeignKey('RightArm', on_delete=models.SET_NULL, null=True, blank=True)
    legs = models.ForeignKey('Legs', on_delete=models.SET_NULL, null=True, blank=True)
    modifiers = models.ManyToManyField('Modifier', blank=True)


    def get_equipped(self):
        return [
            self.helm,
            self.chest,
            self.left_arm,
            self.right_arm,
            self.legs,
        ]


    def get_firepower_value(self):
        firepower_value = 0
        firepower_value += self.left_arm.firepower if self.left_arm else 0
        firepower_value += self.right_arm.firepower if self.right_arm else 0

        return firepower_value


    def get_speed_value(self):

        return self.legs.speed


    def get_armor_value(self):
        armor_value = 0
        for equipment in self.get_equipped():
            armor_value += equipment.armor if equipment else 0

        return armor_value


    def get_sight_value(self):

        return self.helm.sight


    def __str__(self):
        return 'A mobile suit belonging to %s' % self.controller


class Helm(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    sight = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Chest(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class LeftArm(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class RightArm(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Legs(models.Model):
    name = models.CharField(max_length=40, null=True)
    armor = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Modifier(models.Model):
    name = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name