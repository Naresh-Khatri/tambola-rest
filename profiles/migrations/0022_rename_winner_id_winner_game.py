# Generated by Django 3.2.3 on 2021-05-23 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_winner_winner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winner',
            old_name='winner_id',
            new_name='game',
        ),
    ]