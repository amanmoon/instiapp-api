# Generated by Django 3.2.13 on 2022-07-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_auto_20220714_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitypost',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
