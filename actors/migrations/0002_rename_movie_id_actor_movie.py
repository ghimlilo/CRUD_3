# Generated by Django 3.2.9 on 2021-11-17 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
