# Generated by Django 4.2 on 2024-12-03 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_a',
            old_name='a_name',
            new_name='a_last',
        ),
    ]
