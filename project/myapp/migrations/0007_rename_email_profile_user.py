# Generated by Django 5.1.7 on 2025-03-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_customuser_role_profile_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email',
            new_name='user',
        ),
    ]
