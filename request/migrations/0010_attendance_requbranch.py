# Generated by Django 2.2 on 2020-05-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0009_remove_attendance_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='requbranch',
            field=models.CharField(default='comps', max_length=10),
        ),
    ]
