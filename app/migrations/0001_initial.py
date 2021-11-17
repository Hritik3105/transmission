# Generated by Django 3.2.8 on 2021-10-31 09:10

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('domain', models.CharField(default='', max_length=255)),
                ('active', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('patente', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_id', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=255)),
                ('phone', phone_field.models.PhoneField(blank=True, default='', help_text='Contact phone number', max_length=31)),
                ('address', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ins_name', models.CharField(default='', max_length=255)),
                ('days', models.IntegerField(default='', max_length=255)),
                ('vin', models.CharField(default='', max_length=255)),
                ('make', models.CharField(default='', max_length=255)),
                ('paid', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(default='', max_length=255)),
                ('note', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pedimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refrence_id', models.IntegerField(default='', max_length=11)),
                ('pedimento_no', models.IntegerField()),
                ('date', models.DateField()),
                ('importer', models.CharField(default='', max_length=255)),
                ('office', models.CharField(default='', max_length=255)),
                ('signature', models.CharField(default='', max_length=255)),
                ('payment', models.FloatField(default='', max_length=255)),
                ('cove', models.CharField(default='', max_length=255)),
                ('doda', models.CharField(default='', max_length=255)),
                ('ready', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipper_Exports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itn', models.CharField(default='', max_length=11)),
                ('date', models.DateField()),
                ('refrence', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('vin', models.CharField(default='', max_length=255)),
                ('make', models.CharField(default='', max_length=255)),
                ('year', models.IntegerField(default='', max_length=255)),
                ('note', models.CharField(default='', max_length=255)),
                ('paid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Temporary_Permits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permit_date', models.DateField()),
                ('permit_name', models.CharField(default='', max_length=255)),
                ('permit_hour', models.FloatField(default='', max_length=255)),
                ('permit_number', models.CharField(default='', max_length=255)),
                ('permit_vin', models.CharField(default='', max_length=255)),
                ('permit_make', models.CharField(default='', max_length=255)),
                ('permit_year', models.IntegerField(default='', max_length=255)),
                ('permit_note', models.CharField(default='', max_length=255)),
                ('paid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.IntegerField(choices=[('superadmin', 0), ('admin', 1), ('user', 2)], default='2')),
                ('username', models.CharField(default='', max_length=255, verbose_name='username')),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
                ('owner', models.CharField(default='', max_length=255, verbose_name='owner')),
                ('tax_id', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.\t\tUnselect this instead of deleting accounts.')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]