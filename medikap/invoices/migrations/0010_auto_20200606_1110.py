# Generated by Django 3.0.5 on 2020-06-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_invoice_wybrane_uslugi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='wybrane_uslugi',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='usluga',
            field=models.ManyToManyField(to='invoices.ServicesQuantity', verbose_name='usługi'),
        ),
    ]
