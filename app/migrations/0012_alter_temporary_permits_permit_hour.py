# Generated by Django 3.2.8 on 2021-11-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_shipper_exports_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporary_permits',
            name='permit_hour',
            field=models.IntegerField(default='', max_length=255),
        ),
    ]
