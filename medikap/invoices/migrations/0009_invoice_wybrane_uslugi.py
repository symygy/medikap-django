# Generated by Django 3.0.5 on 2020-06-06 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_auto_20200606_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='wybrane_uslugi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invoices.ServicesQuantity'),
            preserve_default=False,
        ),
    ]
