from django.db import models

class Shloka(models.Model):
    chapter = models.PositiveSmallIntegerField()
    shloka_no = models.PositiveSmallIntegerField()
    shloka = models.TextField()
    word_meaning = models.TextField()
    meaning = models.TextField()
    explanation = models.TextField()
    video_url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
      unique_together = (("chapter", "shloka_no"),)