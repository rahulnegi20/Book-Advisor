# Generated by Django 2.1.15 on 2021-05-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210514_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingtime',
            old_name='date_time_field',
            new_name='booking_time',
        ),
    ]
