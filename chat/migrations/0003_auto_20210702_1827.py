# Generated by Django 3.1.3 on 2021-07-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messagenotification_notification_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagenotification',
            name='notification_time',
            field=models.DateTimeField(auto_created=True),
        ),
    ]