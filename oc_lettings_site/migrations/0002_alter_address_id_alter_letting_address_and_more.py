from django.db import migrations


def move_address_and_letting_data(apps, schema_editor):
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    # Créer un mapping pour associer les anciens IDs aux nouveaux IDs
    old_to_new_address = {}

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

    for old_letting in OldLetting.objects.all():
        new_address_id = old_to_new_address.get(old_letting.address_id)
        if new_address_id:
            NewLetting.objects.create(title=old_letting.title, address_id=new_address_id)


def move_profile_data(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(move_address_and_letting_data),
        migrations.RunPython(move_profile_data),
    ]
