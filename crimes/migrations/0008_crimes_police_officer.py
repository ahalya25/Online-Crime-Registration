# Generated by Django 5.2 on 2025-05-20 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimes', '0007_remove_crimes_police_officer'),
        ('police_officers', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crimes',
            name='police_officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='police_officers.policeofficers'),
        ),
    ]
