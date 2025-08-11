from django.shortcuts import render
from .models import Book, Genre, Author
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic

def books(request):
    objects = Book.objects.all()
    paginator = Paginator(objects, per_page=3)
    page_num = request.GET.get("page")
    books = paginator.get_page(page_num)
    return render(request, template_name="books.html", context={"books": books})


def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, template_name="book.html", context={"book": book})


class AuthorListView(generic.ListView):
    model = Author
    template_name = "authors.html"
    context_object_name = "authors"
    paginate_by = 2


def search(request):
    query = request.GET.get("q")
    context = {
        "books": Book.objects.filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)),
        "authors": Author.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)),
        "query": query,
    }
    return render(request, template_name="search.html", context=context)
