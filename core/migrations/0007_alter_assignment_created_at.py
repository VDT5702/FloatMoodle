# Generated by Django 3.2.8 on 2021-10-23 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_assignment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 9, 32, 45, 226281, tzinfo=utc)),
        ),
    ]