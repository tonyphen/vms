# Generated by Django 3.2.5 on 2021-07-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='length',
            name='id',
        ),
        migrations.AlterField(
            model_name='length',
            name='mm',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='MM'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CBM_Feet',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='CBM/Feet'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='M2_Feet',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=18, verbose_name='M2/Feet'),
        ),
    ]