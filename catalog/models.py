from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=300, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f" - {self.description[:100]}. . ."

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class BlogPost(models.Model):
    name = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug')
    description = models.TextField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

