# Generated by Django 3.0.5 on 2020-05-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20200527_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='rabat',
            field=models.IntegerField(blank=True, null=True, verbose_name='rabat [%]'),
        ),
    ]
