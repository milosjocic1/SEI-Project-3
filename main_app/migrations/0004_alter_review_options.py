# Generated by Django 4.1.1 on 2022-10-02 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-content']},
        ),
    ]