# Generated by Django 2.1.15 on 2021-05-10 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Advisor'),
        ),
    ]
