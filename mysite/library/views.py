from django.shortcuts import render
from .models import Book, Genre, Author

def books(request):
    books = Book.objects.all()
    return render(request, template_name="books.html", context={"books": books})

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, template_name="book.html", context={"book": book})