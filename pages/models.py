from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название новости'
    )

    short_description = models.TextField(
        verbose_name='Краткое описание'
    )

    description = models.TextField(
        verbose_name='Полное описание'
    )

    preview_image = models.CharField(
        max_length=255,
        verbose_name='Изображение-превью'
    )

    full_image = models.CharField(
        max_length=255,
        verbose_name='Полное изображение'
    )

    published_at = models.DateField(
        verbose_name='Дата публикации'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return self.title