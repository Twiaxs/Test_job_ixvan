from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from users.managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    username = models.CharField(_('username'), unique=True, max_length=255)
    salary = models.IntegerField(verbose_name="Зарплата", default=0)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f"{self.last_name} {self.first_name}"
        return full_name.strip()

