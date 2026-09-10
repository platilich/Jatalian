from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Word


@login_required
def home(request):
    if request.method == 'POST':
        italian = request.POST.get('italian')
        translation = request.POST.get('translation')

        if italian and translation:
            Word.objects.create(
                user=request.user,
                italian_word=italian,
                translate_word=translation
            )

    words = Word.objects.filter(user=request.user)
    return render(request, 'index.html', {'words': words})