from django.db import models


class Responses(models.Model):

    appeal = models.OneToOneField(
        "appeals.Appeals",
        verbose_name="Обращение",
        on_delete=models.PROTECT,
        blank=False
    )

    response_content = models.TextField(
        blank=False,
        verbose_name="Содержание ответа"
    )

    image = models.ImageField(
        upload_to='images/static/responses/imagination',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    file = models.FileField(
        upload_to='documents/static/responses/',
        blank=True,
        null=True,
        verbose_name="Прикрепляемый документ"
    )

    def get_absolute_url(self):
        return "/responses/"

    def __str__(self):
        return "Ответ № %s " % self.id + ", на: %s" % self.appeal

    class Meta:
        verbose_name_plural = "Ответы на обращения"
        verbose_name = "Ответ на обращение"
