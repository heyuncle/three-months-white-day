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
        'correct_message': 'Correct answer!',
        'correct_color': '#0f0',
        'redirect_url': reverse('index2'),
        'final_page': False,
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
        'final_page': False,
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
        'final_page': False,
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
        'correct_answer': 'whiteday',
        'correct_message': 'Correct, but come back tomorrow!',
        'correct_color': 'orange',
        'redirect_url': reverse('index5'),
        'final_page': False,
    })

def index5(request):
    text_lines = [
        ("C", "happy white day!! well, now that it's almost over, i have some kind of secret i will share with you."),
        ("M", "oh, what kind of secret?"),
        ("C", "i really am happy to share because it's a wonderful surprise to see your shoes and your spirits rise"),
        ("M", "my... shoes?"),
        ("C", "yes! so don't walk away, don't walk away!"),
        ("M", "i won't!"),
        ("C", "because walking back to you is the hardest thing that i can do"),
        ("M", "......"),
        ("C", "but really, i just want to kiss you in new places."),
        ("M", "why are you saying strange things all of a sudden?"),
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/nazo5.png',
        'correct_answer': 'jelly',
        'redirect_url': reverse('index6'),
        'final_page': False,
    })

def index6(request):
    # Final page, no submission form
    text_lines = [
        ("C", "happy anniversary and white day!!! i love you!!!")
    ]
    return render(request, 'game/index.html', {
        'text_lines': text_lines,
        'nazo_image': 'game/final.png',  # You can use a special final image or leave as None
        'final_page': True,              # Add a flag to hide the submission form in the template
    })
