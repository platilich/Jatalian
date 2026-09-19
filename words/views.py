from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Word


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')


@login_required
def home(request):
    words = Word.objects.filter(user=request.user)
    return render(request, 'home.html', {'words': words})


@login_required
@require_POST
def delete_word(request, word_id):
    obj = get_object_or_404(Word, id=word_id, user=request.user)
    obj.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok', 'removed': 'ok'})

    return redirect(request.META.get('HTTP_REFERER', 'vocabulary'))


@login_required
@require_POST
def learned_word(request, word_id):
    obj = get_object_or_404(Word, id=word_id, user=request.user)
    obj.is_learned = not obj.is_learned
    obj.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok', 'is_learned': obj.is_learned})

    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
@require_POST
def voice_word(request, word_id):
    get_object_or_404(Word, id=word_id, user=request.user)
    return JsonResponse({'status': 'ok'})


@login_required
def vocabulary(request):
    words = Word.objects.filter(user=request.user).order_by('-id')
    return render(request, 'vocabulary.html', {'words': words})


@login_required
def new_word(request):
    if request.method == 'POST':
        italian = request.POST.get('italian', '').strip()
        translation = request.POST.get('translation', '').strip()

        if italian and translation:
            Word.objects.create(
                user=request.user,
                italian_word=italian,
                translate_word=translation,
            )
        return redirect('new_word')

    return render(request, 'new_word.html')
