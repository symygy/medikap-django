# Generated by Django 3.0.5 on 2020-05-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='data_wystawienia_faktury',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='forma_platnosci',
            field=models.CharField(choices=[('przelew', 'przelew'), ('gotowka', 'gotówka')], max_length=75, verbose_name='forma płatności'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='rabat',
            field=models.IntegerField(blank=True, verbose_name='rabat [%]'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='usluga',
            field=models.ManyToManyField(to='invoices.Service', verbose_name='usługi'),
        ),
    ]