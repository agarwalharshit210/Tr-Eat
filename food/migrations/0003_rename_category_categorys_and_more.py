# Generated by Django 4.2.5 on 2024-05-02 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_rename_regisster_register'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorys',
        ),
        migrations.RenameModel(
            old_name='Sub_Category',
            new_name='Sub_Categorys',
        ),
    ]