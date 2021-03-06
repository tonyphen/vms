# Generated by Django 3.2.5 on 2021-07-30 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_file', '0009_auto_20210730_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='max_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='min_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_profile', to='master_file.profile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='warehouse_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_warehouse', to='master_file.warehouse', verbose_name='Warehouse'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_woodtype', to='master_file.woodtype'),
        ),
    ]
