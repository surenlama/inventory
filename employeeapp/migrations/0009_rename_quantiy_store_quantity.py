# Generated by Django 4.0.6 on 2022-07-21 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0008_store_quantiy_store_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]
