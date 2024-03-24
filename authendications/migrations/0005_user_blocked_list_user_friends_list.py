# Generated by Django 5.0.3 on 2024-03-24 06:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authendications', '0004_user_bio_user_district_user_place_user_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='friends_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
