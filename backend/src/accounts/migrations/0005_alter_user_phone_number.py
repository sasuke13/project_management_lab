# Generated by Django 4.2.6 on 2023-11-29 10:40

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_id_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31, unique=True),
        ),
    ]
