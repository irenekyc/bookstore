from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import handle_file, check_form
from .models import Book
from .serializer import BookSerializer

# Create your views here.
def upload(request):
    if request.method == "POST":
        data = handle_file(request.FILES['file'])
        return render(request, "apis/file.html", {
            'msg': f"new: {data['new']}, updated: {data['update']}, failed: {data['error']}"
        })
    else:
        num_records = Book.objects.all().count()
        return render(request, "apis/file.html", {
            'msg': f'{num_records} records now. Start uploading here'
        })

def create(request):
    if request.method == 'POST':
        form_data = request.POST
        result = check_form(form_data)
        num_record = Book.objects.all().count()
        messages.success(request,f"{result}. Now we have {num_record}")
        return redirect('success')
  
    else:
        return render(request, "apis/form.html")

def success(request):
    storage = messages.get_messages(request)
    message = ""
    for message in storage:
        print(message)
    return render(request, "apis/message.html", { 
        'msg': message
    })

class ListBooks(APIView):
    def get(self, request, *args, **kwargs):
        filtered_books = Book.objects
        if request.query_params.get('title'):
            filtered_books = filtered_books.filter(title__icontains=request.query_params.get('title'))
        if request.query_params.get('priceFrom'):
            filtered_books = filtered_books.filter(price__gte = request.query_params.get('priceFrom'))
        if request.query_params.get('priceUp'):
            filtered_books = filtered_books.filter(price_lte = request.query_params.get('priceUp'))
        if request.query_params.get('availability'):
            filtered_books = filtered_books.filter(availability = request.query_params.get('availability'))
        if request.query_params.get('category'):
             filtered_books = filtered_books.filter(category__iexact = request.query_params.get('category')) 
        books = BookSerializer(filtered_books, many=True)
        return Response(books.data)

def scrapper(request):
    if request.method == "POST":
        return HttpResponse('Starting scrapper')
    else:
        return HttpResponse('Click to start scrapper')