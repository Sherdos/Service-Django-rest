from django.db import models

# Create your models here.


class Service(models.Model):
    title=models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    create = models.DateField(auto_now_add=True, verbose_name='Время создание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    start = models.DateTimeField(auto_now_add=True, verbose_name='Начать')
    end = models.DateTimeField(verbose_name='Конец')
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        
    def __str__(self) -> str:
        return self.title