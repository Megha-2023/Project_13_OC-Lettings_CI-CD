from django.db import migrations


def forwards_func(apps, schema_editor):
    """ Function to create data from old Profile table"""
    # get the model for new app
    profile = apps.get_model("profiles", "Profile")
    User = apps.get_model("auth", "User")
    db_alias = schema_editor.connection.alias


def reverse_func(apps, schema_editor):
    """ Function for roll back of migration"""
    # If rolling back, delete the newly created Profile data
    profile = apps.get_model("profiles", "Profile")
    db_alias = schema_editor.connection.alias

    # Delete the profile data that was created
    profile.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
       ("profiles", "0001_initial")
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
