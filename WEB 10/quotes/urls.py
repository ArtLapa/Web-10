# quotes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('authors/', views.authors_list, name='authors_list'),
    path('quotes/', views.quotes_list, name='quotes_list'),
]

