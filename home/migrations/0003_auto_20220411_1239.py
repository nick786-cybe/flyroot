# Generated by Django 3.2.12 on 2022-04-11 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
