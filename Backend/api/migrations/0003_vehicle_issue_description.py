# Generated by Django 5.1.5 on 2025-01-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_vehicle_issue_description_alter_vehicle_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='issue_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
