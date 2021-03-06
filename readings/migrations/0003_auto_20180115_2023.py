# Generated by Django 2.0.1 on 2018-01-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0002_auto_20180112_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='authString',
            field=models.CharField(max_length=64, verbose_name='Authentication String'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='readingFloat',
            field=models.FloatField(blank=True, verbose_name='Floating Point Reading'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='readingInt',
            field=models.IntegerField(blank=True, verbose_name='Integer Reading'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='displayType',
            field=models.IntegerField(choices=[(1, 'Floating Point Number'), (2, 'Binary, Yes/No'), (0, 'Integer Number')], default=1, verbose_name='Readings Format'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='displayUnits',
            field=models.CharField(choices=[('mW', 'Power: milliWatts'), ('MW', 'Power: MegaWatts'), ('W', 'Power: Watts'), ('%', 'Math: Percentage'), ('kWh', 'Power: KiloWatt Hours'), ('MWh', 'Power: MegaWatt Hours'), ('BYN', 'Binary: Yes/No'), ('mWh', 'Energy: milliWatt Hours'), ('NUM', 'Generic: Number'), ('Wh', 'Power: Watt Hours'), ('mV', 'Voltage: milliVolts'), ('BPN', 'Binary: Present/Missing'), ('A', 'Current: Amps'), ('BAI', 'Binary: Active/Inactive'), ('kW', 'Power: KiloWatts'), ('BOO', 'Binary: On/Off'), ('F', 'Temp: Farenhiet'), ('K', 'Temp: Kelvin'), ('V', 'Voltage: Volts'), ('mA', 'Current: milliAmps'), ('C', 'Temp: Celsius')], default='NUM', max_length=3, verbose_name='Readings Units'),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='displayType',
            field=models.IntegerField(choices=[(1, 'Floating Point Number'), (2, 'Binary, Yes/No'), (0, 'Integer Number')], default=1, verbose_name='Diplay Format'),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='displayUnits',
            field=models.CharField(choices=[('mW', 'Power: milliWatts'), ('MW', 'Power: MegaWatts'), ('W', 'Power: Watts'), ('%', 'Math: Percentage'), ('kWh', 'Power: KiloWatt Hours'), ('MWh', 'Power: MegaWatt Hours'), ('BYN', 'Binary: Yes/No'), ('mWh', 'Energy: milliWatt Hours'), ('NUM', 'Generic: Number'), ('Wh', 'Power: Watt Hours'), ('mV', 'Voltage: milliVolts'), ('BPN', 'Binary: Present/Missing'), ('A', 'Current: Amps'), ('BAI', 'Binary: Active/Inactive'), ('kW', 'Power: KiloWatts'), ('BOO', 'Binary: On/Off'), ('F', 'Temp: Farenhiet'), ('K', 'Temp: Kelvin'), ('V', 'Voltage: Volts'), ('mA', 'Current: milliAmps'), ('C', 'Temp: Celsius')], default='NUM', max_length=3, verbose_name='Display Units'),
        ),
    ]
