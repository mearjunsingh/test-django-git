# Generated by Django 3.2 on 2022-07-13 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
