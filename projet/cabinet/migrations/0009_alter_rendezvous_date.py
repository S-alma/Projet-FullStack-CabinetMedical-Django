# Generated by Django 4.0.5 on 2022-06-04 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0008_alter_rendezvous_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 16, 57, 34, 899331)),
        ),
    ]
