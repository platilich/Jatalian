from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
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
    return render(request, 'home/index.html', {'words': words})



@login_required
def delete_word(request, word_id):
    if request.method == 'POST':
        obj = get_object_or_404(Word, id=word_id, user=request.user)
        obj.delete()

        return JsonResponse({'status': 'os', 'removed': 'ok'})

    return JsonResponse({'status': 'error'}, status=400)





@login_required
def learned_word(request, word_id):
    if request.method == 'POST':
        obj = get_object_or_404(Word, id=word_id, user=request.user)
        obj.is_learned = not obj.is_learned
        obj.save()

        return JsonResponse({'status': 'ok', 'is_learned': obj.is_learned})


    return JsonResponse({'status': 'error'}, status=400)


@login_required
def voice_word(request, word_id):
    print(word_id)


@login_required
def vocabulary(request):
    words = Word.objects.filter(user=request.user).order_by('-id')
    return render(request, 'home/vocabulary.html', {'words': words})


@login_required
def new_word(request):
    return render(request, 'home/new_word.html')


