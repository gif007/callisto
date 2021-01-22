# Generated by Django 3.1.4 on 2021-01-22 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0007_auto_20210122_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilesuit',
            name='chest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.chest'),
        ),
        migrations.AlterField(
            model_name='mobilesuit',
            name='controller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mobilesuit',
            name='helm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.helm'),
        ),
        migrations.AlterField(
            model_name='mobilesuit',
            name='left_arm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.leftarm'),
        ),
        migrations.AlterField(
            model_name='mobilesuit',
            name='legs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.legs'),
        ),
        migrations.AlterField(
            model_name='mobilesuit',
            name='right_arm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.rightarm'),
        ),
    ]
