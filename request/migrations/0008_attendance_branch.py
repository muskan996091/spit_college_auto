# Generated by Django 2.2 on 2020-05-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0007_auto_20200504_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='branch',
            field=models.CharField(default='comps', max_length=10),
        ),
    ]