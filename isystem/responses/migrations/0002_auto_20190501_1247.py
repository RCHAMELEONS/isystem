# Generated by Django 2.0.4 on 2019-05-01 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responses',
            old_name='appeals',
            new_name='appeal',
        ),
    ]
