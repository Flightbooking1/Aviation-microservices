# Generated by Django 4.2.2 on 2023-06-29 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0006_alter_schedule_available_seats"),
    ]

    operations = [
        migrations.RemoveField(model_name="schedule", name="available_seats",),
    ]