from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}|{self.owner}'

class Transactions(models.Model):
    amount = models.PositiveIntegerField(verbose_name='Сумма')
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True , blank=True)
    organization = models.CharField(max_length=255, verbose_name='Организация')
    description = models.CharField(max_length=255, verbose_name="Описание")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True , blank=True)
    
    def __str__(self):
        return f'{self.amount}|{self.time}'