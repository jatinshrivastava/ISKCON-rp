# Generated by Django 3.1.6 on 2021-04-09 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shloka_feed', '0005_auto_20210409_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswermodel',
            old_name='shloka_object',
            new_name='shloka',
        ),
    ]
