from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    # three dummy sentences for testing click-to-advance
    # each entry is (speaker, message)
    text_lines = [
        ("M", "...good morning... wait... where am i?"),
        ("C", "oh, you made it!"),
        ("C", "i'm sure you're wondering what this is all about."),
        ("C", "there are some holidays for us coming up, which may have been on your mind lately."),
        ("C", "but since i've left tokyo for now, i had to resort to the digital medium to celebrate!"),
        ("C", "...well, mostly digital, anyway."),
        ("M", "...???"),
        ("C", "also, as you know, i've also spent a lot of time with algo (the puzzle club) recently."),
        ("C", "and i can't help but be a little bit mean, haha. so i've added a puzzle element to this."),
        ("M", "orz"),
        ("C", "so here's a gift from me! a scavenger hunt/game for our anniversary!"),
        ("C", "here is some more information:"),
        ("C", "1. this game may take a few hours total between tonight and tomorrow, so please plan accordingly."),
        ("C", "2. if you are stuck, you may ask me for help. sorry if i'm not awake!"),
        ("C", "3. if you want to reread anything, you can refresh the website."),
        ("C", "alright, that's it! good luck! the first step will now be displayed below."),
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/nazo1.png',
        'correct_answer': 'sukida',
        'redirect_url': reverse('index2'),
    })


def index2(request):
    # new set of lines for the second scene
    text_lines = [
        ("M", "i did it!"),
        ("C", "congrats! you solved the first puzzle. it'll get harder from here!"),
        ("M", "okay... i'm ready."),
        ("C", "here's your second challenge!"),
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/nazo2.png',
        'correct_answer': 'banksy',
        'redirect_url': reverse('index3'),
    })


def index3(request):
    text_lines = [
        ("M", "hehe i solved it!"),
        ("C", "wow!! you did great."),
        ("C", "here's your next puzzle!"),
        ("M", "wait... this one looks easy!"),
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/nazo3.png',
        'correct_answer': 'anniversary',
        'redirect_url': reverse('index4'),
    })

def index4(request):
    text_lines = [
        ("C", "uh oh......."),
        ("C", "something went wrong......"),
        ("M", "ei!?!"),
        ("C", "it looks like your answer was correct, but then some rocks fell on it!"),
        ("C", "it's no longer correct, so you need a new right answer."),
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/nazo4.png',
        'correct_answer': 'disabled',
        'redirect_url': reverse('index5'),
    })

def index5(request):
    text_lines = [
        ("C", "come back tomorrow!")
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/nazo4.png',
        'correct_answer': 'disabled',
        'redirect_url': reverse('index5'),
    })
