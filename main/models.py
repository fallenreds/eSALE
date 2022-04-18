from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class MyUser(AbstractUser):
    favorite = models.ManyToManyField(
        'Post',
        verbose_name='Избранное',
        blank="True",
        related_name='favorite',)


class Category(MPTTModel):
    """Модель категорий"""
    title = models.TextField('Название', max_length=50)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Модель обьявлений"""
    title = models.TextField('Название обьявления', max_length=50)
    text = models.TextField('Содержимое обьявления', max_length=300)
    image = models.ImageField('Главная фотография', upload_to="main/", blank=True, null=True)
    cost = models.FloatField('Цена', null=False)
    published_date = models.DateTimeField('Дата публикации', default=timezone.now, blank=True, null=True)

    author = models.ForeignKey(
        MyUser,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True)
    viewed = models.ManyToManyField(
        MyUser,
        verbose_name='Просмотрено',
        blank="True",
        related_name='viewed')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

    def get_absolute_url(self):
        return f'/post/{self.id}'


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст", max_length=300)
    created_date = models.DateField(verbose_name="Дата", default=timezone.now, blank=True, null=True)

    author = models.ForeignKey(
        MyUser,
        verbose_name='Автор',
        related_name='author',
        on_delete=models.CASCADE)

    profile = models.ForeignKey(
        MyUser,
        verbose_name='Профиль комметария',
        related_name='profile',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментрации'
