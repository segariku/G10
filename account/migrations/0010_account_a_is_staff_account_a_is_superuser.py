# Generated by Django 4.2 on 2024-12-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_account_a_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_a',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account_a',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
