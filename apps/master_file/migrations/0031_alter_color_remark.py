# Generated by Django 3.2.5 on 2021-08-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0030_alter_color_color_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='remark',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Remark'),
        ),
    ]
