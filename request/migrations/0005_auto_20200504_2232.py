# Generated by Django 2.2 on 2020-05-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_auto_20200504_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='isapproved',
            field=models.BooleanField(),
        ),
    ]
