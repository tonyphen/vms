# Generated by Django 3.2.5 on 2021-08-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0026_product_sort_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'ordering': ('color_group', 'color_id')},
        ),
        migrations.RemoveField(
            model_name='color',
            name='id',
        ),
        migrations.AlterField(
            model_name='color',
            name='color_id',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Code'),
        ),
    ]
