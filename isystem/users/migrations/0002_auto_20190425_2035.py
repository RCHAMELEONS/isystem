# Generated by Django 2.0.4 on 2019-04-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telephone',
        ),
        migrations.AddField(
            model_name='user',
            name='apartment_registration',
            field=models.CharField(default='', max_length=50, verbose_name='Квартира'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city_registration',
            field=models.CharField(default='', max_length=50, verbose_name='Город/село'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='date_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='date_document',
            field=models.DateField(default='2019-01-01', verbose_name='Дата выдачи документа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='house_registration',
            field=models.CharField(default='', max_length=50, verbose_name='Дом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='index_registration',
            field=models.IntegerField(default=0, verbose_name='Индекс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(choices=[('Russian', 'Российская Федерация'), ('Kaz', 'Казахстан'), ('Uk', 'Украина')], default='', max_length=35, verbose_name='Гражданство'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='number_document',
            field=models.IntegerField(default=0, verbose_name='Номер паспорта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='patronymic',
            field=models.CharField(default='', max_length=70, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='7999999999', max_length=17, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='place_document',
            field=models.CharField(default='', max_length=150, verbose_name='Место выдачи документа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(default='', max_length=70, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='series_document',
            field=models.IntegerField(default=0, verbose_name='Серия паспорта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('Man', 'Мужской'), ('Woman', 'Женский')], default='', max_length=8, verbose_name='Пол'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street_registration',
            field=models.CharField(default='', max_length=50, verbose_name='Улица'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=70, verbose_name='Имя'),
        ),
    ]
