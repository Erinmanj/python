# Generated by Django 5.0.6 on 2024-05-29 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_appointment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
    ]
