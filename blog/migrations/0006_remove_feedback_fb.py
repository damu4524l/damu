# Generated by Django 4.1.8 on 2023-04-14 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_feedback_feedback_fb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='fb',
        ),
    ]
