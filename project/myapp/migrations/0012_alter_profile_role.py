# Generated by Django 5.1.7 on 2025-03-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_profile_hit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')], max_length=20, null=True),
        ),
    ]
