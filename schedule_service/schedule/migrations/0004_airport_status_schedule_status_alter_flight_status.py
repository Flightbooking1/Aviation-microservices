# Generated by Django 4.2.2 on 2023-06-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0003_alter_airport_id_alter_flight_id_alter_schedule_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="airport",
            name="status",
            field=models.CharField(default="Active", max_length=45),
        ),
        migrations.AddField(
            model_name="schedule",
            name="status",
            field=models.CharField(default="Active", max_length=45),
        ),
        migrations.AlterField(
            model_name="flight",
            name="status",
            field=models.CharField(default="Active", max_length=45),
        ),
    ]
