# Generated by Django 5.1.2 on 2024-11-21 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShowtimeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='theater_location',
        ),
    ]