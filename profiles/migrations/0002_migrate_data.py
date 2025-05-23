from django.db import migrations


def forwards_func(apps, schema_editor):
    """ Function to create data from old Profile table"""
    # get the model for new app
    profile = apps.get_model("profiles", "Profile")
    User = apps.get_model("auth", "User")
    db_alias = schema_editor.connection.alias

    # get the model from old app
    # old_profile = apps.get_model("oc_lettings_site", "Profile")

    # for each object in old app table create new object in new app table
    """for profile_obj in old_profile.objects.using(db_alias).all():
        user = profile_obj.user
        profile.objects.using(db_alias).create(
            user=user,
            favorite_city=profile_obj.favorite_city,
        )"""

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
