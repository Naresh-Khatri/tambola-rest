# Generated by Django 3.2.3 on 2021-05-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_alter_game_drawn_numbers_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='last_played_winner',
        ),
        migrations.AlterField(
            model_name='game',
            name='drawn_numbers_list',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='game',
            name='last_played_num',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
