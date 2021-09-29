from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from users.constants import GENDER_CHOICES, COUNTRY_CODES, COUNTRY_NAMES
import uuid


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    country_code = models.CharField(max_length=16, choices=COUNTRY_CODES, default='+91')
    phone_number = models.CharField(max_length=12, unique=True)
    address = models.CharField(verbose_name="Address line", max_length=1024, blank=True, null=True)
    country_name = models.CharField(max_length=2, choices=COUNTRY_NAMES, default='IN', blank=True)
    birth_date = models.DateField(verbose_name="Date of birth", blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='P')
    email_verified = models.BooleanField(blank=False, default=False)
    REQUIRED_FIELDS = ['email', 'country_code', 'phone_number']

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


@receiver(pre_save, sender=CustomUser)
def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4()
models.signals.pre_save.connect(random_username, sender=CustomUser)