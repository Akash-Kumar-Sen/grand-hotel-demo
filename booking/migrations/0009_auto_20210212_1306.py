# Generated by Django 3.0.3 on 2021-02-12 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_apartment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='apartment_image',
            new_name='room_image',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='apartment_no',
            new_name='room_no',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='apartment_type',
            new_name='room_type',
        ),
    ]
