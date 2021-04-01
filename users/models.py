from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# # from django.contrib.auth.backends import ModelBackend
# # from django.db.models import Q


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    address = models.CharField(verbose_name="Address line", max_length=1024, blank=True, null=True)
    birth_date = models.DateField(verbose_name="Date of birth", blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='P')
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:  # to allow authentication through phone number or any other field, modify the below statement
#             user = CustomUser.objects.get(Q(phone_number__iexact=username) | Q(email__iexact=username))
#         except CustomUser.DoesNotExist:
#             CustomUser().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
#
#     def get_user(self, user_id):
#         try:
#             user = CustomUser.objects.get(pk=user_id)
#         except CustomUser.DoesNotExist:
#             return None
#
#         return user if self.user_can_authenticate(user) else None
