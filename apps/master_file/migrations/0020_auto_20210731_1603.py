# Generated by Django 3.2.5 on 2021-07-31 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0019_auto_20210731_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_profile', to='master_file.profile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_unit', to='master_file.unit', verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_warehouse', to='master_file.warehouse', verbose_name='Warehouse'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_woodtype', to='master_file.woodtype'),
        ),
    ]
