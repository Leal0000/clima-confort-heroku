# Generated by Django 2.2.12 on 2021-05-20 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='clave',
            new_name='clave_nueva',
        ),
    ]
