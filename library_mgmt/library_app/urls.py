from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('add/', views.add_book, name='add_book'),
    path('issue/', views.issue_book, name='issue_book'),
    path('return/', views.return_book, name='return_book'),
]