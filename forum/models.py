from django.db import models
from django.db.models.deletion import CASCADE, PROTECT


class Address(models.Model):
    """Адрес."""
    street = models.CharField(max_length=255, verbose_name='улица')
    suite = models.CharField(max_length=255, verbose_name='квартира')
    city = models.CharField(max_length=255, verbose_name='город')
    zipcode = models.CharField(max_length=10, verbose_name='почтовый индекс')
    lat = models.FloatField(verbose_name='широта')
    lng = models.FloatField(verbose_name='долгота')

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'


class Company(models.Model):
    """Компания."""
    name = models.CharField(max_length=255, unique=True)
    catchphrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class User(models.Model):
    """Пользователь форума."""
    external_id = models.IntegerField(unique=True, verbose_name='внешний идентификатор')
    name = models.CharField(max_length=255, verbose_name='имя')
    username = models.CharField(max_length=255, unique=True, verbose_name='логин')
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=32, verbose_name='номер телефона')
    website = models.URLField(verbose_name='веб-сайт')

    address = models.ForeignKey(Address, on_delete=PROTECT, related_name='users')
    company = models.ForeignKey(Company, on_delete=PROTECT, related_name='users')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Post(models.Model):
    """Публикация."""
    external_id = models.IntegerField(unique=True, verbose_name='внешний идентификатор')
    title = models.CharField(max_length=255, verbose_name='заголовок')
    body = models.TextField(verbose_name='пост')
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='posts', verbose_name='пользователь')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

