# Generated by Django 5.0.1 on 2024-09-24 05:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_youtubevideo_delete_aboutvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmap',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmap',
            name='map_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmap',
            name='title',
            field=models.CharField(default='https://example.com/map', max_length=200),
            preserve_default=False,
        ),
    ]