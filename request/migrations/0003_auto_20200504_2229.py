# Generated by Django 2.2 on 2020-05-04 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20200504_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='isapproved',
        ),
    ]