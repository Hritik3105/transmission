# Generated by Django 3.2.8 on 2021-11-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_inventories_pedimentorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='released',
            name='file',
            field=models.CharField(default='', max_length=255),
        ),
    ]
