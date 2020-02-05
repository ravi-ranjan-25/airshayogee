# Generated by Django 3.0.2 on 2020-02-05 08:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cab', '0004_auto_20200205_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='caborder',
            name='pickuplat',
            field=models.CharField(default='0.00', max_length=256),
        ),
        migrations.AddField(
            model_name='caborder',
            name='pickuplong',
            field=models.CharField(default='0.00', max_length=256),
        ),
        migrations.AddField(
            model_name='caborder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='caborder',
            name='latitude',
            field=models.CharField(default='0.00', max_length=256),
        ),
        migrations.AlterField(
            model_name='caborder',
            name='longitude',
            field=models.CharField(default='0.00', max_length=256),
        ),
        migrations.AlterField(
            model_name='caborder',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 8, 27, 27, 436938, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tax',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 8, 27, 27, 436217, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usermob',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 8, 27, 27, 434594, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='cabDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.CharField(max_length=256)),
                ('CabModel', models.CharField(max_length=256)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 2, 5, 8, 27, 27, 435237, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
