# Generated by Django 5.1.1 on 2024-09-23 12:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_remove_item_completed_at_remove_item_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
