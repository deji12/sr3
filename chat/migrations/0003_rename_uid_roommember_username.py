# Generated by Django 5.0.4 on 2024-05-01 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roommember',
            old_name='uid',
            new_name='username',
        ),
    ]
