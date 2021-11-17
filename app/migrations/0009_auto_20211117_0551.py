# Generated by Django 3.2.8 on 2021-11-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_shipper_exports_itn'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='Type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='insurance',
            name='policy_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]