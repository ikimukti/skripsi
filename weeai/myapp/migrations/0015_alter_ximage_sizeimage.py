# Generated by Django 4.2.1 on 2023-05-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_exposurecorrection_ximage_distanceobject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ximage',
            name='sizeImage',
            field=models.JSONField(null=True),
        ),
    ]
