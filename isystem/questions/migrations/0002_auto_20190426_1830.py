# Generated by Django 2.0.4 on 2019-04-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='theme',
            field=models.CharField(max_length=150, verbose_name='Тема вопроса'),
        ),
    ]
