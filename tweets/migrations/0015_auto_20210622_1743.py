# Generated by Django 3.1.3 on 2021-06-22 17:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0014_delete_tweetlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='_tweet_likes_+', to=settings.AUTH_USER_MODEL),
        ),
    ]