# Generated by Django 3.2.3 on 2021-05-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_alter_game_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='last_played_winner',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
