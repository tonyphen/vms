# Generated by Django 3.2.5 on 2021-08-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0035_alter_color_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='wood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='woodtype_color', to='master_file.woodtype', verbose_name='Wood Type'),
        ),
    ]
