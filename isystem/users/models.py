from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Вы должны ввести email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    NATIONALITY = (
        ('Russian', 'Российская Федерация'),
        ('Kaz', 'Казахстан'),
        ('Uk', 'Украина')
    )

    SEX = (
        ('Man', 'Мужской'),
        ('Woman', 'Женский')
    )

    second_name = models.CharField(
        max_length=80,
        verbose_name="Фамилия"
    )

    first_name = models.CharField(
        max_length=80,
        verbose_name="Имя"
    )

    patronymic = models.CharField(
        max_length=80,
        verbose_name="Отчество"
    )

    date_birth = models.DateField(
        verbose_name="Дата рождения"
    )

    sex = models.CharField(
        max_length=8,
        verbose_name="Пол",
        choices=SEX
    )

    phone_number = models.CharField(
        max_length=17,
        verbose_name='Телефон'
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    nationality = models.CharField(
        max_length=35,
        verbose_name="Гражданство",
        choices=NATIONALITY

    )

    series_document = models.IntegerField(
        verbose_name="Серия паспорта"
    )

    number_document = models.IntegerField(
        verbose_name="Номер паспорта"
    )

    date_document = models.DateField(
        verbose_name="Дата выдачи документа"
    )

    place_document = models.CharField(
        max_length=150,
        verbose_name="Место выдачи документа"
    )

    index_registration = models.IntegerField(
        verbose_name="Индекс"
    )

    city_registration = models.CharField(
        max_length=50,
        verbose_name="Город/село",
    )

    street_registration = models.CharField(
        max_length=50,
        verbose_name="Улица",
    )

    house_registration = models.CharField(
        max_length=50,
        verbose_name="Дом",
    )

    apartment_registration = models.CharField(
        max_length=50,
        verbose_name="Квартира",
    )

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(
        default=False,
        verbose_name='Статус пользователя',
        help_text='Отметьте, если пользователь может входить в административную часть сайта.'
    )

    object = UserManager()
    objects = models.Manager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return "/lk/"

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'