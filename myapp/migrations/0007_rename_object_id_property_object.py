# Generated by Django 5.2 on 2025-04-13 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_object_property_object_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='object_id',
            new_name='object',
        ),
    ]
