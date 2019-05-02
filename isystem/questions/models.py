from django.db import models


class Questions(models.Model):

    people = models.ForeignKey(
        "users.User",
        verbose_name="Гражданин",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    theme = models.CharField(
        max_length=150,
        blank=False,
        verbose_name="Тема вопроса"
    )

    content_question = models.TextField(
        blank=False,
        verbose_name="Содержание вопроса"
    )

    image = models.ImageField(
        upload_to='images/static/questions/imagination',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    file = models.FileField(
        upload_to='documents/static/questions/',
        blank=True,
        null=True,
        verbose_name="Прикрепляемый документ"
    )

    def get_absolute_url(self):
        return "/questions/"

    def __str__(self):
        return "Вопрос № %s" % self.id + ", от: %s" % self.people.second_name + ' ' + self.people.first_name

    class Meta:
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"

