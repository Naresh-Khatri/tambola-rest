# Generated by Django 3.2.3 on 2021-05-23 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_ticket_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='winner_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='winner_game', to='profiles.game'),
        ),
    ]