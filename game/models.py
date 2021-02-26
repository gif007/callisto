from django.db import models
from django.contrib.auth.models import  User
from django.http import JsonResponse

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


    def attack(self, opponent):
        """Diminish opponents current health"""
        import random
        damage = random.randint(self.firepower-3, self.firepower+3)
        dps = damage * self.firerate
        effective_damage = dps
        opponent.current_hp -= effective_damage
        opponent.save()

        return opponent.current_hp


    def generateLoot(self):
        """Generate a loot table"""
        loot = {
            'coins': 42,
            'leather scraps': 3,
        }

        return loot


    def die(self):
        """Called when felled in battle"""
        loot = self.generateLoot()
        data = {
            'loot': loot,
            'enemy_health': '0 / %s' % (self.max_hp),
        }
        self.delete()

        return JsonResponse(data)


    def __str__(self):
        """Returns a string the represent the current instance"""
        return self.name


