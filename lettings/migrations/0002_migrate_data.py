from django.db import migrations


def forwards_func(apps, schema_editor):
    """ Function to create data from old Profile table"""
    # get the model for new app
    new_address = apps.get_model("lettings", "Address")
    new_letting = apps.get_model("lettings", "Letting")
    db_alias = schema_editor.connection.alias

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
