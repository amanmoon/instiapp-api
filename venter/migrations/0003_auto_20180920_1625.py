# Generated by Django 2.0.7 on 2018-09-20 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("venter", "0002_auto_20180917_1648"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complaintmedia",
            name="complaint",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="venter.Complaints",
            ),
        ),
    ]
