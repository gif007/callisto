# Generated by Django 3.1.4 on 2021-01-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20210122_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='trinket',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
