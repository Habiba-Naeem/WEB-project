# Generated by Django 2.2.13 on 2020-08-20 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20200820_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='avg_rating',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
