# Generated by Django 3.2.8 on 2021-10-23 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211023_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='feedback',
        ),
        migrations.AddField(
            model_name='assignmentsubmission',
            name='feedback',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 6, 32, 36, 75946, tzinfo=utc)),
        ),
    ]
