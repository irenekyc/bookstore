from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apis.models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(books, 50)
    if page_num == None:
        page_num = 1
    page_obj = paginator.get_page(page_num)
    return render(request, "books/index.html", {
        'books': page_obj
    })

def category(request):
    categories = [category[0] for category in Book.objects.values_list('category').distinct()]
    return render(request, "books/category.html", { 
        'categories': sorted(categories)
    })

def category_list(request, category_name):
    filtered_books = Book.objects.filter(category__iexact = category_name)
    return render(request, "books/category_list.html", {
        'category': category_name,
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

def about(request):
    return render(request, "about.html")