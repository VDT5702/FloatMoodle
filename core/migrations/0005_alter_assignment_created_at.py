# Generated by Django 3.2.8 on 2021-10-23 06:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211023_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 6, 54, 52, 712565, tzinfo=utc)),
        ),
    ]
