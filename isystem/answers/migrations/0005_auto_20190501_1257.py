# Generated by Django 2.0.4 on 2019-05-01 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0004_auto_20190501_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Ответ на вопрос', 'verbose_name_plural': 'Ответы на вопросы'},
        ),
    ]
