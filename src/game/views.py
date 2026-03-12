from django.shortcuts import render


# Create your views here.

def get_index():
    # no parameters required for this simple view
    return {}

def index(request):
    # three dummy sentences for testing click-to-advance
    # each entry is (speaker, message)
    text_lines = [
        ("C", "Welcome to the RPG world!"),
        ("M", "The journey begins with a single step."),
        ("C", "Click to continue the adventure..."),
    ]
    return render(request, 'game/index.html', {'text_lines': text_lines})
