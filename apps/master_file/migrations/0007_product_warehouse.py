# Generated by Django 3.2.5 on 2021-07-30 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_file', '0006_alter_thick_mm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Code')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('credit_acc', models.IntegerField(blank=True, null=True, verbose_name='credit code')),
                ('debit_acc', models.IntegerField(blank=True, null=True, verbose_name='debit code')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Code')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='master_file.profile')),
                ('warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='master_file.warehouse', verbose_name='Warehouse')),
                ('wood_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='master_file.woodtype')),
            ],
        ),
    ]
