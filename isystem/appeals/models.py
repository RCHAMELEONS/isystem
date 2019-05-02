from django.db import models


class Appeals(models.Model):

    people = models.ForeignKey(
        "users.User",
        verbose_name="Гражданин",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    theme = models.CharField(
        max_length=128,
        blank=False,
        verbose_name="Тема обращения"
    )

    content_appeals = models.TextField(
        blank=False,
        verbose_name="Содержание обращения"
    )

    image = models.ImageField(
        upload_to='images/static/appeals/imagination',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    file = models.FileField(
        upload_to='documents/static/appeals/',
        blank=True,
        null=True,
        verbose_name="Прикрепляемый документ"
    )

    def get_absolute_url(self):
        return "/appeals/"

    def __str__(self):
        return "Обращение № %s" % self.id + ", от: %s" % self.people.second_name + ' ' + self.people.first_name

    class Meta:
        verbose_name_plural = "Обращения"
        verbose_name = "Обращение"

