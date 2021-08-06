# Generated by Django 3.2.5 on 2021-08-04 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0027_auto_20210804_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_color', to='master_file.color', verbose_name='Color'),
        ),
    ]