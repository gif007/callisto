from django.test import TestCase

from .models import MobileSuit, LeftArm, RightArm, Legs, Chest, Helm

# Create your tests here.


class MobileSuitModelTests(TestCase):
    
    def test_get_firepower_value_with_empty_slot(self):
        """Tests that correct firepower is returned even with empty slots"""
        left_arm = LeftArm(name='spam', firepower=1)
        right_arm = RightArm(name='bacon', firepower=1)
        suit = MobileSuit(name='eggs')
        """No weapons should return no firepower"""
        self.assertIs(suit.get_firepower_value(), 0)
        """Now testing each slot individually"""
        suit.left_arm=left_arm
        self.assertIs(suit.get_firepower_value(), 1)

        suit.left_arm=None # Remove left_arm weapon to test right_arm on its own
        suit.right_arm=right_arm
        self.assertIs(suit.get_firepower_value(), 1)


    def test_get_armor_value_with_empty_slots(self):
        """Tests that the correct armor value is returned even with empty slots"""
        suit = MobileSuit(name='eggs')
        left_arm = LeftArm(name='spam', armor=1)
        right_arm = RightArm(name='bacon', armor=1)
        legs = Legs(name='arthur', armor=1)
        chest = Chest(name='swallow', armor=1)
        helm = Helm(name='monty', armor=1)
        """No equipment should return no armor"""
        self.assertIs(suit.get_armor_value(), 0)
        """Now testing to ensure that armor increments with additional equipment"""
        suit.left_arm = left_arm
        self.assertIs(suit.get_armor_value(), 1)

        suit.right_arm = right_arm
        self.assertIs(suit.get_armor_value(), 2)

        suit.helm = helm
        self.assertIs(suit.get_armor_value(), 3)

        suit.chest = chest
        self.assertIs(suit.get_armor_value(), 4)

        suit.legs = legs
        self.assertIs(suit.get_armor_value(), 5)


    def test_get_speed_value_with_empty_slot(self):
        """Tests that get_speed_value returns properly even with empty slot"""
        suit = MobileSuit(name='eggs')
        self.assertIs(suit.get_speed_value(), 0)
        legs = Legs(name='spam', speed=1)
        suit.legs = legs
        self.assertIs(suit.get_speed_value(), 1)


    def test_get_sight_value_with_empty_slot(self):
        """Tests that get_speed_sight returns properly even with empty slot"""
        suit = MobileSuit(name='eggs')
        self.assertIs(suit.get_sight_value(), 0)
        helm = Helm(name='spam', sight=1)
        suit.helm = helm
        self.assertIs(suit.get_sight_value(), 1)