# Generated by Django 3.1.4 on 2021-01-22 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210122_0208'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Controller',
        ),
        migrations.AddField(
            model_name='chest',
            name='armor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chest',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='helm',
            name='armor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='helm',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='leftarm',
            name='armor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leftarm',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='legs',
            name='armor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='legs',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='rightarm',
            name='armor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rightarm',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
