# Generated by Django 3.2.3 on 2021-05-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_ticker_id_ticket_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='bought_by',
            field=models.CharField(blank=True, default='Not Booked', max_length=100),
        ),
    ]
