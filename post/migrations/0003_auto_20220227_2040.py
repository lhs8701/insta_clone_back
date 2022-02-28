# Generated by Django 3.1.3 on 2022-02-27 11:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_bookmark_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmark_user_set',
            field=models.ManyToManyField(blank=True, related_name='bookmark_user_set', through='post.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='like_user_set', through='post.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
