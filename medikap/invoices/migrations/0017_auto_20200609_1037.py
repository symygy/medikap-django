# Generated by Django 3.0.5 on 2020-06-09 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0016_invoice_usluga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceitem',
            old_name='usluga',
            new_name='usluga_fk',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='usluga',
        ),
    ]