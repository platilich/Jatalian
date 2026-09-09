from django.contrib import admin

from .models import Word, UserWord


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('italian_word', 'translate_word', 'created')
    search_fields = ('italian_word', 'translate_word')


@admin.register(UserWord)
class UserWordAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'is_learned')

