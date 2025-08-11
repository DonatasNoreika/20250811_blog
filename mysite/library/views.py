from django.shortcuts import render
from .models import Book, Genre, Author
from django.core.paginator import Paginator

def books(request):
    objects = Book.objects.all()
    paginator = Paginator(objects, per_page=3)
    page_num = request.GET.get("page")
    books = paginator.get_page(page_num)
    return render(request, template_name="books.html", context={"books": books})

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, template_name="book.html", context={"book": book})