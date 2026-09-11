from django.db import models
from django.conf import settings


# Create your models here.
class Word(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='words')

    italian_word = models.CharField(max_length=100, verbose_name='Word')
    translate_word = models.CharField(max_length=100, verbose_name='Translation')


    is_learned = models.BooleanField(default=False)


    created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')



    def __str__(self):
        return self.italian_word