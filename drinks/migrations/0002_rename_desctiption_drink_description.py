# Generated by Django 5.0.6 on 2024-07-04 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='desctiption',
            new_name='description',
        ),
    ]
