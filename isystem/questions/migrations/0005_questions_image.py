# Generated by Django 2.0.4 on 2019-04-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20190427_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/static/questions/imagination', verbose_name='Изображение'),
        ),
    ]
