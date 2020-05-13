# Generated by Django 2.2 on 2020-05-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20200504_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='branch',
            field=models.CharField(default='comps', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='isapproved',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
    ]