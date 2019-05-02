# Generated by Django 2.0.4 on 2019-04-25 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.TextField(verbose_name='Содержание ответа')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='questions.Questions', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
