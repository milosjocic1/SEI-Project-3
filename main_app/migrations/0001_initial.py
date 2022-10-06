# Generated by Django 4.1.1 on 2022-10-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('keywords', models.CharField(max_length=20)),
            ],
        ),
    ]
