
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("books/<int:book_id>", views.book, name="book"),
    path("search/", views.search, name='search'),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
]
