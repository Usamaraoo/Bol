# Generated by Django 3.1.3 on 2021-06-21 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweetlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetlike',
            name='tweet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tweets.tweet'),
        ),
    ]