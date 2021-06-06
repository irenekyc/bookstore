from django.shortcuts import render, get_object_or_404
from apis.models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {
        'books': books[0:10]
    })

def category(request):
    categories = [category[0] for category in Book.objects.values_list('category').distinct()]
    return render(request, "books/category.html", { 
        'categories': categories
    })

def category_list(request, category_name):
    filtered_books = Book.objects.filter(category__iexact = category_name)
    return render(request, "books/category_list.html", {
        'books': filtered_books
    })

def book_details(request, book_slug):
    try:
        book = Book.objects.get(slug=book_slug)
        return render(request, "books/details.html", {
            'book': book
        })
    except Book.DoesNotExist:
        return render(request, "books/details.html", {
            'error': 'Book Not Found'
        })