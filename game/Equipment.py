from django.db import models

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