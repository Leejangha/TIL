# Generated by Django 4.2.6 on 2023-10-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finlife', '0004_alter_depositoptions_intr_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoptions',
            name='fin_prdt_cd',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='depositoptions',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
    ]
