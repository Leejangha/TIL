# Generated by Django 4.2.7 on 2023-11-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.CharField(max_length=255, unique=True)),
                ('cur_nm', models.CharField(max_length=255)),
                ('tts', models.CharField(max_length=255)),
                ('deal_bas_r', models.CharField(max_length=255)),
            ],
        ),
    ]
