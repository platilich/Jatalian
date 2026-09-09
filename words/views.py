from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Word


@login_required
def home(request):
    words = Word.objects.all().order_by('italian_word')
    return render(request, 'index.html', {'words': words})

