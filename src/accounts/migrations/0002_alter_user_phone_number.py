# Generated by Django 4.2.6 on 2023-11-27 20:29

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]