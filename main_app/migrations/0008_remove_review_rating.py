# Generated by Django 4.1.1 on 2022-10-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_destination_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
