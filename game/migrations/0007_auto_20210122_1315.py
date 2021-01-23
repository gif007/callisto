# Generated by Django 3.1.4 on 2021-01-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_trinket_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trinket',
            new_name='Modifier',
        ),
        migrations.RemoveField(
            model_name='mobilesuit',
            name='trinkets',
        ),
        migrations.AddField(
            model_name='mobilesuit',
            name='modifiers',
            field=models.ManyToManyField(to='game.Modifier'),
        ),
    ]