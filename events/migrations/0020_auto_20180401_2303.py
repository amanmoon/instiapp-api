# Generated by Django 2.0.3 on 2018-04-01 17:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0019_auto_20180329_1256"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ("-time_of_creation",),
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
            },
        ),
    ]
