# Generated by Django 3.2.13 on 2022-10-03 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0014_location_str_id'),
        ('bodies', '0023_body_canonical_name'),
        ('users', '0040_remove_userprofile_followed_communities'),
        ('community', '0027_auto_20221003_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitypost',
            name='view_count',
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='followed_by',
            field=models.ManyToManyField(blank=True, related_name='followedposts', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='ignored',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communityposts', to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='tag_body',
            field=models.ManyToManyField(blank=True, related_name='taggedcommunityposts', to='bodies.Body'),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='tag_location',
            field=models.ManyToManyField(blank=True, related_name='taggedcommunityposts', to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='tag_user',
            field=models.ManyToManyField(blank=True, related_name='taggedcommunitypost', to='users.UserProfile'),
        ),
    ]
