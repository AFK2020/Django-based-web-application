# Generated by Django 5.1.7 on 2025-03-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_rename_email_profile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="ip_address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
