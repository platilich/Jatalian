from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

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




def delete_word(request, word_id):
    obj = get_object_or_404(Word, id=word_id, user=request.user)
    obj.delete()


    return redirect('home')



def learned_word(request, word_id):
    obj = get_object_or_404(Word, id=word_id, user=request.user)
    obj.is_learned = not obj.is_learned
    obj.save()

    return redirect('home')