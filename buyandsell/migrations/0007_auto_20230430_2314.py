# Generated by Django 3.2.16 on 2023-04-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyandsell', '0006_auto_20230430_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
