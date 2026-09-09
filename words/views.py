from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Word


@login_required
def home(request):
    words = Word.objects.first()



    return render(request, 'index.html', {'words': words})



def next_word(request):
    words = Word.objects.order_by('?').first()

    context = {
        'words': [words] if words else []
    }


    return render(request, 'index.html', {'words': context})