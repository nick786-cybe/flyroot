# Generated by Django 3.2.12 on 2022-04-13 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='timestamp',
        ),
    ]
