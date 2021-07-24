# Generated by Django 3.2.5 on 2021-07-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0003_auto_20210723_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feet', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Feet')),
                ('inch', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Inch')),
                ('mm', models.IntegerField(blank=True, default=0, null=True, verbose_name='MM')),
                ('freqUsed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Freq. used')),
            ],
        ),
    ]
