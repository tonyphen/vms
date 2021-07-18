# Generated by Django 3.2.5 on 2021-07-18 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_healthcheckitem_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcheckitem',
            name='cong_ty',
            field=models.CharField(choices=[('VINAWOOD', 'VINAWOOD'), ('Other', 'Other')], default='', max_length=100, verbose_name='Công ty'),
        ),
        migrations.AlterField(
            model_name='healthcheckitem',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Bộ phận'),
        ),
    ]