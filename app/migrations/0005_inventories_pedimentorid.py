# Generated by Django 3.2.8 on 2021-11-02 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_released_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventories',
            name='pedimentorid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pedimentos'),
        ),
    ]
