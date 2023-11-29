# Generated by Django 4.2.6 on 2023-11-27 16:17

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('states', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('NW', 'New'), ('REG', 'Registered'), ('APPR', 'Approved'), ('SNT', 'Sent'), ('DLV', 'Delivered'), ('PD', 'Paid'), ('CNL', 'Canceled')], default='NW')),
                ('grant_date', models.DateField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('order_history', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='orders.states')),
            ],
        ),
    ]