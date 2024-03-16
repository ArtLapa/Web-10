from django.shortcuts import render, redirect
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

def register(request):
    # Реєстрація користувача - код на ваш вибір

    def login(request):
    # Вхід користувача - код на ваш вибір

        def add_author(request):
         if request.method == 'POST':
            form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на головну сторінку
        else:
            form = AuthorForm()
        return render(request, 'add_author.html', {'form': form})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на головну сторінку
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'quotes': quotes})

def home(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all()
    return render(request, 'home.html', {'authors': authors, 'quotes': quotes})
