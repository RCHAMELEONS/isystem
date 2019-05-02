from django.db import models


class Answers(models.Model):

    question = models.OneToOneField(
        "questions.Questions",
        verbose_name="Вопрос",
        on_delete=models.PROTECT,
        blank=False
    )

    answer_content = models.TextField(
        blank=False,
        verbose_name="Содержание ответа"
    )

    image = models.ImageField(
        upload_to='images/static/answers/imagination',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    file = models.FileField(
        upload_to='documents/static/answers/',
        blank=True,
        null=True,
        verbose_name="Прикрепляемый документ"
    )

    def get_absolute_url(self):
        return "/answers/"

    def __str__(self):
        return "Ответ № %s " % self.id + ", на: %s" % self.question

    class Meta:
        verbose_name_plural = "Ответы на вопросы"
        verbose_name = "Ответ на вопрос"
