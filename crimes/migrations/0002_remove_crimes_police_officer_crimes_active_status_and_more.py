# Generated by Django 5.2 on 2025-05-16 06:40

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crimes',
            name='police_officer',
        ),
        migrations.AddField(
            model_name='crimes',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='crimes',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crimes',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='crimes',
            name='uuid',
            field=models.SlugField(default=uuid.uuid4, editable=False),
        ),
    ]
