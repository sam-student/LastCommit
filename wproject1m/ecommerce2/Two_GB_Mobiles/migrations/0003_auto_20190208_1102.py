# Generated by Django 2.0 on 2019-02-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two_GB_Mobiles', '0002_auto_20190208_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Audio',
            field=models.TextField(default='3.5mm audio jack, MP4/WMV/H.264 player'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='BuiltIn',
            field=models.TextField(default='16GB Built-in'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Data',
            field=models.TextField(default='GPRS, Edge, 3G (HSPA 42.2/5.76 Mbps), 4G (LTE-A (2CA) Cat6 300/50 Mbps'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Dimension',
            field=models.TextField(default='146.2 x 71.3 x 8 mm'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Front',
            field=models.TextField(default='13 MP, f/1.9, LED flash'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='GPU',
            field=models.TextField(default='Mali-T830MP2 '),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Main',
            field=models.TextField(default='8MP'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='NFC',
            field=models.TextField(default='Yes'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='OperatingSystem',
            field=models.TextField(default='Android v7.1 Nougat'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Protection',
            field=models.TextField(default='Yes'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Resolution',
            field=models.TextField(default='720 x 1280 Pixels (~282 PPI) '),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='Size',
            field=models.TextField(default='5.5 inches'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='TwoGBand',
            field=models.TextField(default='SIM1: GSM 850 / 900 / 1800 / 1900 SIM2: GSM 850 / 900 / 1800 / 1900  '),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='UIBuild',
            field=models.TextField(default='TouchWiz UI'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='USB',
            field=models.TextField(default='microUSB 2.0'),
        ),
        migrations.AlterField(
            model_name='two_gb_mobile',
            name='card',
            field=models.TextField(default='Yes'),
        ),
    ]
