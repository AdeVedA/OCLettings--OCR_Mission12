# Generated by Django 5.1.5 on 2025-01-21 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0002_alter_address_id_alter_letting_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
