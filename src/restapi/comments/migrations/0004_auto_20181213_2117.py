# Generated by Django 2.0.7 on 2018-12-13 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20181213_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 13, 21, 17, 20, 102879)),
        ),
        migrations.AlterField(
            model_name='replies',
            name='replied_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 13, 21, 17, 20, 106792)),
        ),
    ]
