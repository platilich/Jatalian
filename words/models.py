from django.db import models
from django.conf import settings

# Create your models here.
class Word(models.Model):
    italian_word = models.CharField(max_length=100, verbose_name='Word')
    translate_word = models.CharField(max_length=100, verbose_name='Translation')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')



    def __str__(self):
        return self.italian_word




class UserWord(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_words'
    )
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        related_name='user_words'
    )
    is_learned = models.BooleanField(
        default=False,
        verbose_name='Learned'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'word'],
                name='unique_user_word'
            )
        ]

    def __str__(self):
        return f'{self.user} — {self.word}'