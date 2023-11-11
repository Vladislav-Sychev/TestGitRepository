from typing import Collection
from django.db import models

# Create your models here.

class Hall(models.Model): 
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Выставочный зал'
        verbose_name_plural = 'Выставочные залы'

class Collection(models.Model): 
        name = models.CharField(max_length=100, verbose_name='Название') 
        description = models.TextField(verbose_name='Краткое описание') 
        hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name='Зал') 
        start_date = models.DateField(verbose_name='Дата начала') 
        end_date = models.DateField(verbose_name='Дата окончания')

        def __str__(self):
            return self.name


        class Meta:
            verbose_name = 'Коллекция'
            verbose_name_plural = 'Коллекции'


class Exhibit(models.Model): 
    name = models.CharField(max_length=100, verbose_name='Название') 
    description = models.TextField(verbose_name='Краткое описание') 
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая стоимость') 
    century = models.IntegerField(verbose_name='Век создания') 
    collection = models.ForeignKey(Collection ,on_delete=models.CASCADE, verbose_name='Коллекция') 
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Высота') 
    width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ширина') 
    length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Длина') 
    temperature_control = models.BooleanField(verbose_name='Необходимость контроля температуры') 
    humidity_control = models.BooleanField(verbose_name='Необходимость контроля влажности')
    protection = models.BooleanField(verbose_name='Защищённость от людей')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экспонат'
        verbose_name_plural = 'Экспонаты'

