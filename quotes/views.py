from django.shortcuts import render

# Create your views here.

import random

def home(request):
    quotes = [
        "Believe you can and you're halfway there.",
        "Your limitation—it’s only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn’t just find you. You have to go out and get it."
    ]
    selected_quote = random.choice(quotes)
    return render(request, 'quotes/home.html', {'quote': selected_quote})

def about(request):
    return render(request, 'quotes/about.html')

def contact(request):
    return render(request, 'quotes/contact.html')
