# Generated by Django 4.1.3 on 2023-11-17 21:12

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capyba', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='primeiro_nome',
        ),
        migrations.AddField(
            model_name='usuario',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(default=datetime.datetime(2023, 11, 17, 21, 12, 13, 561916, tzinfo=datetime.timezone.utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default=datetime.datetime(2023, 11, 17, 21, 12, 22, 846417, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
    ]