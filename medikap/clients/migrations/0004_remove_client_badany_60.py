# Generated by Django 3.0.5 on 2020-04-22 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20200421_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='badany_60',
        ),
    ]
