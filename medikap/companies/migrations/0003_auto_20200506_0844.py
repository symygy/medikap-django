# Generated by Django 3.0.5 on 2020-05-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20200505_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data_dodania',
            field=models.DateTimeField(auto_now_add=True, default='2020-05-06 08:44:21'),
            preserve_default=False,
        ),
    ]
