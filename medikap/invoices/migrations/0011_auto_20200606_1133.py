# Generated by Django 3.0.5 on 2020-06-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0010_auto_20200606_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='usluga',
            field=models.ManyToManyField(to='invoices.Service', verbose_name='usługi'),
        ),
    ]
