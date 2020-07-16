# Generated by Django 3.0.5 on 2020-06-06 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_auto_20200528_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.PositiveIntegerField()),
                ('usluga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Service')),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='usluga',
            field=models.ManyToManyField(to='invoices.ServicesQuantity', verbose_name='usługi'),
        ),
    ]