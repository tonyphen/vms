# Generated by Django 3.2.5 on 2021-07-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0007_alter_length_freqused'),
    ]

    operations = [
        migrations.AlterField(
            model_name='length',
            name='freqUsed',
            field=models.BooleanField(verbose_name='Freq. used'),
        ),
    ]
