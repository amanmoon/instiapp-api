# Generated by Django 2.0.3 on 2018-03-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0018_event_bodies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
