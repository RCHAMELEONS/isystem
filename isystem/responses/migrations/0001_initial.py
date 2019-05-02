# Generated by Django 2.0.4 on 2019-05-01 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appeals', '0004_auto_20190501_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_content', models.TextField(verbose_name='Содержание ответа')),
                ('appeals', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='appeals.Appeals', verbose_name='Обращение')),
            ],
            options={
                'verbose_name': 'Ответ на обращение',
                'verbose_name_plural': 'Ответы на обращения',
            },
        ),
    ]
