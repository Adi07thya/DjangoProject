# Generated by Django 3.0.4 on 2020-05-13 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmark_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
