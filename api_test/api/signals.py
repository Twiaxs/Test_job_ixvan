from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User
from api.models import Category


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    cat = ["Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование", "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд"]
    for caterory in cat:
        Category.objects.create(owner=instance, name=caterory)
        
