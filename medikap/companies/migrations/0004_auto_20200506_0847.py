# Generated by Django 3.0.5 on 2020-05-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20200506_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data_dodania',
            field=models.DateTimeField(auto_now=True),
        ),
    ]