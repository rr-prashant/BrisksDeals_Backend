# Generated by Django 4.1.6 on 2023-02-23 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brisk_app1', '0005_rename_full_name_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='full_name',
        ),
    ]
