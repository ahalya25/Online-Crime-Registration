# Generated by Django 5.2 on 2025-05-16 06:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_officers', '0003_alter_policeofficers_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeofficers',
            name='uuid',
            field=models.SlugField(default=uuid.uuid4, editable=False),
        ),
    ]
