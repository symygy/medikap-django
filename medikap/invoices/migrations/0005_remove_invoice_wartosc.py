# Generated by Django 3.0.5 on 2020-05-28 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_invoice_wartosc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='wartosc',
        ),
    ]