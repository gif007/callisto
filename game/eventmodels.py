from django.db import models


class EventSuper(models.Model):
    """Describes an Event that occurs in the Outlands"""
    name = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def getActions(self):
        """Returns a list of actions to be utilized by front-end"""
        return []

    def serialize(self):
        """Returns a serialization for json"""
        return {
            'name': self.name,
            'desc': self.desc
        }

    def __str__(self):
        """Returns a string representation of the Event"""
        return self.name


class EventNothing(EventSuper):
    """Describes an event about nothing"""

    def getActions(self):
        return ['Continue']


class EventDiscovery(EventSuper):
    """Describes a discovery event"""
    discovered = models.CharField(max_length=50, null=True, blank=True)

    def getActions(self):
        return ['Continue', 'Examine']

    def serialize(self):
        """Returns a serialization for json"""
        return {
            'name': self.name,
            'desc': self.desc,
            'discovered': self.discovered
        }


class EventBattle(EventSuper):
    """Describes a battle event"""
    enemy = models.ForeignKey('Enemy', on_delete=models.SET_NULL, null=True, blank=True)

    def getActions(self):
        return ['Attack', 'Flee']

    def serialize(self):
        """Returns a serialization for json"""
        return {
            'name': self.name,
            'desc': self.desc,
            'enemy': self.enemy.name
        }