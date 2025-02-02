from django.db import migrations


def move_address_and_letting_data(apps, schema_editor):
    """
    Transfers data from the Address and Letting models of the 'oc_lettings_site' application
    to the new models in the 'lettings' application.

    This function maps old Address records to new Address records and preserves the
    relationship between Lettings and their associated Addresses.

    Args:
        apps: Provides access to the models at the current state of the migration.
        schema_editor: The database schema editor (not used in this function but required).
    """
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    old_to_new_address = {}

    # Migrate Address data and store a mapping of old IDs to new IDs
    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        old_to_new_address[old_address.id] = new_address.id

    # Migrate Letting data and use the mapping to associate with new Address records
    for old_letting in OldLetting.objects.all():
        new_address_id = old_to_new_address.get(old_letting.address_id)
        if new_address_id:
            NewLetting.objects.create(title=old_letting.title, address_id=new_address_id)


def move_profile_data(apps, schema_editor):
    """
    Transfers data from the Profile model of the 'oc_lettings_site' application
    to the new Profile model in the 'profiles' application.

    This function ensures that Profile records maintain their association with the
    corresponding User and transfers the 'favorite_city' field.

    Args:
        apps: Provides access to the models at the current state of the migration.
        schema_editor: The database schema editor (not used in this function but required).
    """
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    # Migrate Profile data
    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):
    """
    Migration class to transfer data from the old 'oc_lettings_site' application
    to the new 'lettings' and 'profiles' applications.

    Dependencies:
        - Requires the initial migrations for 'lettings' and 'profiles' to be applied.
        - Assumes data exists in the 'oc_lettings_site' application.
    """

    dependencies = [
        ("lettings", "0001_initial"),
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(move_address_and_letting_data),
        migrations.RunPython(move_profile_data),
    ]
