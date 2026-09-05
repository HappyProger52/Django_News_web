from django.contrib.auth.models import User
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


class Role(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название роли'
    )

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Код роли'
    )

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_role',
        verbose_name='Пользователь'
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Роль'
    )

    def __str__(self):
        return f'{self.user.username} — {self.role.name}'


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Статья'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пользователь'
    )

    text = models.TextField(
        verbose_name='Текст комментария'
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
        return f'Комментарий от {self.user.username}'