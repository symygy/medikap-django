# Generated by Django 3.1.3 on 2021-02-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20200528_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='regon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='REGON'),
        ),
    ]
