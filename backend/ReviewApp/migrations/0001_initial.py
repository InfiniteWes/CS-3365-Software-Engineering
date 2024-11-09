# Generated by Django 5.1.2 on 2024-11-09 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MovieApp', '0001_initial'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('review_text', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
            ],
        ),
    ]