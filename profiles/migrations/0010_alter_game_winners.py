# Generated by Django 3.2.3 on 2021-05-22 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_game_winners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winners',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.winner'),
        ),
    ]
