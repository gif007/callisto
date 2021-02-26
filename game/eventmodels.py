from django.db import models


class EventSuper(models.Model):
    """Describes an Event that occurs in the Outlands"""
    name = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.CharField(max_length=100, null=True, blank=True)

    def getActions(self):
        """Returns a list of actions to be utilized by front-end"""
        return []

    def serialize(self):
        """Returns a serialization for json"""
        return {
            'name': self.name,
            'desc': self.desc,
            'img': self.img,
        }

    def __str__(self):
        """Returns a string representation of the Event"""
        return self.name


class EventNothing(EventSuper):
    """Describes an event about nothing"""

    def getActions(self):
        return ['continue']





class EventDiscovery(EventSuper):
    """Describes a discovery event"""
    discovered = models.CharField(max_length=50, null=True, blank=True)

    def getActions(self):
        return ['continue', 'examine']

    def serialize(self):
        """Returns a serialization for json"""
        return {
            'name': self.name,
            'desc': self.desc,
            'discovered': self.discovered,
            'img': self.img,
        }


class EventBattle(EventSuper):
    """Describes a battle event"""
    enemy = models.ForeignKey('Enemy', on_delete=models.SET_NULL, null=True, blank=True)

    def getActions(self):
        return ['engage', 'flee']

    def serialize(self):
        """Returns a serialization for json"""
        return {
            'name': self.name,
            'desc': self.desc,
            'enemy': self.enemy.name,
            'img': self.img,
        }