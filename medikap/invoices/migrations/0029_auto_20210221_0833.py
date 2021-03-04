# Generated by Django 3.1.3 on 2021-02-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0028_invoice_termin_platnosci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='termin_platnosci',
            field=models.IntegerField(blank=True, choices=[(7, '7 dni'), (14, '14 dni'), (21, '21 dni')], null=True, verbose_name='termin płatności'),
        ),
    ]