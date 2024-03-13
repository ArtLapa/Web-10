# quotes/urls.py
from django.urls import path
from .views import register, add_author, add_quote, authors_list, quotes_list

urlpatterns = [
    path('register/', register, name='register'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
    path('authors/', authors_list, name='authors_list'),
    path('quotes/', quotes_list, name='quotes_list'),
]
