# Generated by Django 3.2.8 on 2021-11-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_insurance_policy_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='insurer',
            field=models.CharField(default='', max_length=255),
        ),
    ]