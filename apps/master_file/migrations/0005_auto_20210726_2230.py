# Generated by Django 3.2.5 on 2021-07-26 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0004_auto_20210726_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='woodtype',
            old_name='freqUse',
            new_name='freqUsed',
        ),
        migrations.RenameField(
            model_name='woodtype',
            old_name='type',
            new_name='prod_type',
        ),
    ]
