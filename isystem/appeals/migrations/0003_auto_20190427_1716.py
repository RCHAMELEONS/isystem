# Generated by Django 2.0.4 on 2019-04-27 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0002_auto_20190427_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeals',
            name='people',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Гражданин'),
        ),
    ]
