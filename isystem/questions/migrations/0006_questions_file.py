# Generated by Django 2.0.4 on 2019-04-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_questions_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/static/questions/', verbose_name='Прикрепляемый документ'),
        ),
    ]
