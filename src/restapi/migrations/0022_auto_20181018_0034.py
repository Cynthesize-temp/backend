# Generated by Django 2.0.7 on 2018-10-17 19:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0021_auto_20181008_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 0, 34, 43, 709368)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 0, 34, 43, 708195)),
        ),
        migrations.AlterField(
            model_name='upvoted_ideas',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='upvoted_ideas', to=settings.AUTH_USER_MODEL),
        ),
    ]
