# Generated by Django 4.1 on 2022-08-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing_pages", "0004_remove_landingpageentry_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="landingpageentry",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
