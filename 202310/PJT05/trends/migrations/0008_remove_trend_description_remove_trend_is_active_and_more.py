# Generated by Django 4.2.6 on 2023-10-13 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0007_trend_keyword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trend',
            name='description',
        ),
        migrations.RemoveField(
            model_name='trend',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='trend',
            name='name',
        ),
        migrations.AddField(
            model_name='trend',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
