# Generated by Django 3.0.5 on 2020-05-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20200527_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='wartosc',
            field=models.FloatField(blank=True, null=True),
        ),
    ]