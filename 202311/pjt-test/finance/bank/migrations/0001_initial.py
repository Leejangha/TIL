# Generated by Django 4.2.7 on 2023-11-16 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=255, unique=True)),
                ('kor_co_nm', models.CharField(max_length=255)),
                ('fin_prdt_nm', models.CharField(max_length=255)),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField(choices=[(1, '제한없음'), (2, '서민전용'), (3, '일부제한')])),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=255, unique=True)),
                ('kor_co_nm', models.CharField(max_length=255)),
                ('fin_prdt_nm', models.CharField(max_length=255)),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField(choices=[(1, '제한없음'), (2, '서민전용'), (3, '일부제한')])),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('mtrt_int', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('save_trm', models.IntegerField()),
                ('rsrv_type_nm', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='bank.savingproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='bank.depositproducts')),
            ],
        ),
    ]
