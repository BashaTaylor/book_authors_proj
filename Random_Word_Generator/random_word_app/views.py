from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
# def index(request):
#     return redirect('/random_words')

def rand_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['word'] = get_random_string(length=14)
    request.session['count'] += 1
    return render(request, 'random_word.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')