# Generated by Django 4.2.1 on 2023-05-23 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_date_ximage_datecreated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ximage',
            name='edgeDetection',
        ),
    ]
