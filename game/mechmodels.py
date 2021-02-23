from django.db import models
from django.contrib.auth.models import  User


class MobileSuit(models.Model):
    """An object representing a mobile suit fitted with equipment"""
    name = models.CharField(max_length=40, null=True)
    max_hp = models.IntegerField(default=0)
    current_hp = models.IntegerField(default=0)
    controller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    helm = models.ForeignKey('Helm', on_delete=models.SET_NULL, null=True, blank=True)
    chest = models.ForeignKey('Chest', on_delete=models.SET_NULL, null=True, blank=True)
    left_arm = models.ForeignKey('LeftArm', on_delete=models.SET_NULL, null=True, blank=True)
    right_arm = models.ForeignKey('RightArm', on_delete=models.SET_NULL, null=True, blank=True)
    legs = models.ForeignKey('Legs', on_delete=models.SET_NULL, null=True, blank=True)
    modifiers = models.ManyToManyField('Modifier', blank=True)


    def get_equipped(self):
        """Returns a list representing the occupancy of the equipment slots"""
        return [
            self.helm,
            self.chest,
            self.left_arm,
            self.right_arm,
            self.legs,
        ]


    def get_firepower_value(self):
        """Returns the sum of all firepower"""
        firepower_value = 0
        firepower_value += self.left_arm.firepower if self.left_arm else 0
        firepower_value += self.right_arm.firepower if self.right_arm else 0

        return firepower_value


    def get_firerate_value(self):
        """Returns the sum of all firerate"""
        firerate_value = 0
        firerate_value += self.left_arm.firerate if self.left_arm else 0
        firerate_value += self.right_arm.firerate if self.right_arm else 0

        return firerate_value


    def get_speed_value(self):
        """Returns suit speed"""
        return self.legs.speed if self.legs else 0


    def get_armor_value(self):
        """Returns the sum of all armor values"""
        armor_value = 0
        for equipment in self.get_equipped():
            armor_value += equipment.armor if equipment else 0

        return armor_value


    def get_sight_value(self):
        """Return field visibility"""
        return self.helm.sight if self.helm else 0


    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class Helm(models.Model):
    """A piece of equipment to be equipped to the head slot"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    armor = models.IntegerField(default=0)
    sight = models.IntegerField(default=0)
    img = models.CharField(max_length=50, null=True, blank=True)

    def serialize(self):
        """Returns a serialization of attributes for JSON"""
        return {
            'name': self.name,
            'desc': self.desc,
            'armor': self.armor,
            'sight': self.sight,
        }

    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class Chest(models.Model):
    """A piece of equipment to be worn in the chest slot"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    armor = models.IntegerField(default=0)
    img = models.CharField(max_length=50, null=True, blank=True)

    def serialize(self):
        """Returns a serialization of attributes for JSON"""
        return {
            'name': self.name,
            'desc': self.desc,
            'armor': self.armor,
        }

    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class LeftArm(models.Model):
    """The left arm weapon"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    armor = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)
    firerate = models.FloatField(default=1.0)
    img = models.CharField(max_length=50, null=True, blank=True)

    def serialize(self):
        """Returns a serialization of attributes for JSON"""
        return {
            'name': self.name,
            'desc': self.desc,
            'armor': self.armor,
            'firepower': self.firepower,
            'firerate': self.firerate,
        }

    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class RightArm(models.Model):
    """The right arm weapon"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    armor = models.IntegerField(default=0)
    firepower = models.IntegerField(default=0)
    firerate = models.FloatField(default=1.0)
    img = models.CharField(max_length=50, null=True, blank=True)

    def serialize(self):
        """Returns a serialization of attributes for JSON"""
        return {
            'name': self.name,
            'desc': self.desc,
            'armor': self.armor,
            'firepower': self.firepower,
            'firerate': self.firerate,
        }

    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class Legs(models.Model):
    """A piece of equipment that is responsible for moving the suit"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    armor = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    img = models.CharField(max_length=50, null=True, blank=True)

    def serialize(self):
        """Returns a serialization of attributes for JSON"""
        return {
            'name': self.name,
            'desc': self.desc,
            'armor': self.armor,
            'speed': self.speed,
        }

    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


class Modifier(models.Model):
    """A piece of equipment that may grant user additional abilities"""
    name = models.CharField(max_length=40, null=True)
    desc = models.TextField(null=True)
    img = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name