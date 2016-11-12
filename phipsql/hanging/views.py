from django.shortcuts import render
from django.http import HttpResponse
from . import models, hanged
import random

def index(request):
    return render(request, 'hanging/index.html')

def game(request):
    models.Word.objects.all().delete()
    models.Right.objects.all().delete()
    models.Wrong.objects.all().delete()
    models.Terminal.objects.all().delete()
    w = hanged.chosen()
    i = models.Word(word = w, rgt = len(w), wrg = 6)
    i.save()
    for l in w:
        e = models.Right(word = i, letter = l)
        e.save()
    res = models.Responds.objects.filter(situation = 'start').filter(ratio = 1)
    r = random.choice(res)
    t = models.Terminal(text = r)
    t.save()
    terminal = models.Terminal.objects.all()
    letters = models.Right.objects.all()
    holder = []
    for l in letters:
        if l.state == True:
            holder += [l.letter]
        else:
            holder += ['_']

    wh = " ".join(holder)
    hangedMan = hanged.hangedMan(0)
    return render(request, 'hanging/hanging.html', { 'terminal': terminal, 'holder': wh, 'hangedMan': hangedMan })


def loop(request):
    word = models.Word.objects.all()
    W = word[0].word
    wordLen = len(W)
    right = models.Right.objects.all()
    letter = request.POST['letter']
    ratio = 1
    ### generalCheck ###
    state = hanged.valid(letter, word[0].word)
    if state == 'compWin':
        res = models.Responds.objects.filter(situation = state).filter(ratio = 1)
        r = random.choice(res)
        return render(request, 'hanging/end.html', { 'respond': r , 'word': W})
    elif state == 'right':
        for i in right:
            if i.letter == letter:
                i.state = True
                i.save()
    elif state == 'wrong':
        wrg = models.Wrong(word = word[0], letter = letter)
        wrg.save()


    ### lostCheck ###
    wrgs = models.Wrong.objects.all()
    if len(wrgs) >= 6:
        state = 'lost'
        res = models.Responds.objects.filter(situation = state).filter(ratio = 1)
        r = random.choice(res)
        return render(request, 'hanging/end.html', { 'respond': r , 'word': W })


    ### winCheck ###
    num = 0
    for r in right:
        if r.state == True:
            num += 1
    if num == wordLen:
        state = 'win'
        res = models.Responds.objects.filter(situation = state).filter(ratio = 1)
        r = random.choice(res)
        return render(request, 'hanging/end.html', { 'respond': r , 'word': W})

    ### nextRound ###
    t = models.Terminal(text = '>>> {}'.format(letter))
    t.save()
    #if state == 'right':
        #ratio = num
    if state == 'wrong' and len(wrgs) <= 2:
        ratio = 1

    if state == 'wrong' and len(wrgs) > 2 and len(wrgs) <= 4:
        ratio = 2

    if state == 'wrong' and len(wrgs) > 4:
        ratio = 3

    res = models.Responds.objects.filter(situation = state).filter(ratio = ratio)
    r = random.choice(res)
    tr = models.Terminal(text = r)
    tr.save()
    terminal = list(models.Terminal.objects.all())
    while len(terminal) > 10:
        terminal.pop(0)

    holder = []
    for l in right:
        if l.state == True:
            holder += [l.letter]
        else:
            holder += ['_']
    wh = " ".join(holder)

    wng = []
    for l in wrgs:
        wng += [l.letter]
    wrong = " ".join(wng)

    hangedMan = hanged.hangedMan(len(wrgs))
    return render(request, 'hanging/hanging.html', { 'terminal': terminal, 'holder': wh,
                            'hangedMan': hangedMan, 'wrong': wrong })
