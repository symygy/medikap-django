# Generated by Django 3.0.5 on 2020-07-21 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('invoices', '0024_auto_20200713_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uslugi',
            field=models.ManyToManyField(to='services.Service', verbose_name='usługi'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='usluga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]