# Generated by Django 3.2 on 2023-02-23 14:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0003_auto_20230223_1250"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="agent",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="agent",
            name="last_name",
        ),
    ]
