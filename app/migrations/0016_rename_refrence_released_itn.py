# Generated by Django 3.2.8 on 2021-11-24 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_insurance_insurer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='released',
            old_name='refrence',
            new_name='itn',
        ),
    ]
