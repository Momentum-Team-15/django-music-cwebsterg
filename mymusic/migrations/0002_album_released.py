# Generated by Django 4.1.2 on 2022-10-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='released',
            field=models.DateField(blank=True, null=True),
        ),
    ]
