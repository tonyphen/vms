# Generated by Django 3.2.5 on 2021-07-28 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_file', '0003_alter_profilemaster_group_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='length',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='length_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='length',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='length_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortgroup',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sort_group_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortgroup',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sort_group_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thick',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='thick_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thick',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='thick_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='woodtype',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='wood_type_creator', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='woodtype',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='wood_type_updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilemaster',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_master_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profilemaster',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_master_updater', to=settings.AUTH_USER_MODEL),
        ),
    ]
