# Generated by Django 4.2.2 on 2023-06-23 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(name="airport", table="airport",),
        migrations.AlterModelTable(name="flight", table="flight",),
        migrations.AlterModelTable(name="schedule", table="schedule",),
    ]