# Generated by Django 5.1.7 on 2025-03-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_remove_customuser_role_profile_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="role",
        ),
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("gold", "Gold"), ("silver", "Silver"), ("bronze", "Bronze")],
                default="Unauthenticated",
                max_length=20,
                null=True,
            ),
        ),
    ]
