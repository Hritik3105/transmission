# Generated by Django 3.2.8 on 2021-12-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencies',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='pedimentos',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='provider',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='released',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='shipper_exports',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='temporary_permits',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
    ]
