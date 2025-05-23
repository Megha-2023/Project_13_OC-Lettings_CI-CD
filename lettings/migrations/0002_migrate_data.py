from django.db import migrations


def forwards_func(apps, schema_editor):
    """ Function to create data from old Profile table"""
    # get the model for new app
    new_address = apps.get_model("lettings", "Address")
    new_letting = apps.get_model("lettings", "Letting")
    db_alias = schema_editor.connection.alias

    # get the model from old app
    # old_address = apps.get_model("oc_lettings_site", "Address")
    # old_letting = apps.get_model("oc_lettings_site", "Letting")

    # for each object in old app table create new object in new app table
    address_map = {}
    """for address_obj in old_address.objects.using(db_alias).all():
        new_address_obj = new_address.objects.using(db_alias).create(
            number=address_obj.number,
            street=address_obj.street,
            city=address_obj.city,
            state=address_obj.state,
            zip_code=address_obj.zip_code,
            country_iso_code=address_obj.country_iso_code,
        )
        address_map[address_obj.id] = new_address_obj
    
    for letting_obj in old_letting.objects.using(db_alias).all():
        address = letting_obj.address.id
        new_address_obj = address_map.get(address)
        new_letting.objects.using(db_alias).create(
            title=letting_obj.title,
            address=new_address_obj,
        )"""

def reverse_func(apps, schema_editor):
    """ Function for roll back of migration"""
    # If rolling back, delete the newly created Address and Letting data
    new_address = apps.get_model("lettings", "Address")
    new_letting = apps.get_model("lettings", "Letting")
    db_alias = schema_editor.connection.alias

    # Delete the Address and Letting data that was created
    new_address.objects.using(db_alias).all().delete()
    new_letting.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
       ("lettings", "0001_initial")
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
