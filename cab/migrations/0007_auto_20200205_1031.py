# Generated by Django 3.0.2 on 2020-02-05 10:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0006_auto_20200205_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabdetail',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 10, 31, 7, 296724, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caborder',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 10, 31, 7, 298808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tax',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 10, 31, 7, 297907, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usermob',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 10, 31, 7, 296050, tzinfo=utc)),
        ),
    ]
