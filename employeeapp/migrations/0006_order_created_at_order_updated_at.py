# Generated by Django 4.0.6 on 2022-07-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0005_category_image_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateField(null=True),
        ),
    ]
