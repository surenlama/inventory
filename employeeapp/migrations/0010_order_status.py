# Generated by Django 4.0.6 on 2022-07-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0009_rename_quantiy_store_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Client', 'Client'), ('Staff', 'Staff'), ('Crew', 'Crew'), ('Member', 'Member')], max_length=255, null=True, verbose_name='Status'),
        ),
    ]
