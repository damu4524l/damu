# Generated by Django 4.1.8 on 2023-04-14 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogs',
            new_name='feedback',
        ),
    ]
