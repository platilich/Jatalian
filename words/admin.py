from django.contrib import admin
from .models import Word



@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('italian_word', 'translate_word', 'user', 'created')
    search_fields = ('italian_word', 'translate_word')