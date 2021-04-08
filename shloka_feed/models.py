from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.core.validators import RegexValidator

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
from users.constants import ANSWER_CHOICES


class Shloka(models.Model):
    chapter = models.PositiveSmallIntegerField()
    shloka_no = models.PositiveSmallIntegerField()
    shloka = models.TextField()
    word_meaning = models.TextField()
    meaning = models.TextField()
    explanation = models.TextField()
    video_url = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    quizIsActive = models.BooleanField(blank=False, default=False)

    class Meta:
        unique_together = (("chapter", "shloka_no"),)


class QuizModel(models.Model):
    chapter = models.PositiveSmallIntegerField(blank=False)
    shloka_no = models.PositiveSmallIntegerField(blank=False)
    shloka_id = models.ForeignKey('shloka_feed.Shloka', on_delete=models.CASCADE, blank=False)
    question = models.TextField(blank=False)
    optionA = models.TextField(blank=False, verbose_name="Option A")
    optionB = models.TextField(blank=False, verbose_name="Option B")
    optionC = models.TextField(blank=False, verbose_name="Option C")
    optionD = models.TextField(blank=False, verbose_name="Option D")
    answer = models.CharField(blank=False, choices=ANSWER_CHOICES, default='A', max_length=1)
    point = models.PositiveSmallIntegerField(blank=False, default=5)