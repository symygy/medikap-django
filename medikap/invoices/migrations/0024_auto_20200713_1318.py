# Generated by Django 3.0.5 on 2020-07-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0023_auto_20200616_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uslugi',
            field=models.ManyToManyField(to='invoices.Service', verbose_name='usługi'),
        ),
    ]