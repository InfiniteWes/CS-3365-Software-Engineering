# Generated by Django 5.1.2 on 2024-11-21 05:32

import UserApp.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(default='', max_length=150, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('has_credit_card', models.BooleanField(default=False)),
                ('credit_card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('credit_card_expiration', models.DateField(blank=True, null=True)),
                ('credit_card_cvv', models.CharField(blank=True, max_length=3, null=True)),
                ('credit_card_billing', models.CharField(blank=True, max_length=100, null=True)),
                ('has_debit_card', models.BooleanField(default=False)),
                ('debit_card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('debit_card_expiration', models.DateField(blank=True, null=True)),
                ('debit_card_cvv', models.CharField(blank=True, max_length=3, null=True)),
                ('debit_card_billing', models.CharField(blank=True, max_length=100, null=True)),
                ('has_paypal', models.BooleanField(default=False)),
                ('paypal_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', UserApp.models.CustomUserManager()),
            ],
        ),
    ]
