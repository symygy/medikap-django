# Generated by Django 3.0.5 on 2020-04-24 05:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0003_auto_20200424_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='data_odpowiedzi',
            field=models.DateField(blank=True, default=datetime.date(2020, 4, 24)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='data_odczytania',
            field=models.DateField(blank=True),
        ),
    ]
