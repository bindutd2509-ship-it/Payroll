import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('legal_name', models.CharField(blank=True, max_length=200)),
                ('registration_number', models.CharField(blank=True, max_length=100, unique=True)),
                ('pan_number', models.CharField(blank=True, max_length=20)),
                ('tan_number', models.CharField(blank=True, max_length=20)),
                ('pf_number', models.CharField(blank=True, max_length=50)),
                ('esi_number', models.CharField(blank=True, max_length=50)),
                ('professional_tax_number', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('pincode', models.CharField(blank=True, max_length=20)),
                ('timezone', models.CharField(default='UTC', max_length=50)),
                ('currency', models.CharField(default='INR', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('financial_year_start_month', models.IntegerField(default=4)),
                ('payroll_cycle', models.CharField(default='Monthly', max_length=50)),
                ('pf_enabled', models.BooleanField(default=False)),
                ('esi_enabled', models.BooleanField(default=False)),
                ('professional_tax_enabled', models.BooleanField(default=False)),
                ('tds_enabled', models.BooleanField(default=False)),
                ('attendance_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='companies.company')),
            ],
            options={
                'verbose_name_plural': 'Company Settings',
                'db_table': 'company_settings',
            },
        ),
    ]