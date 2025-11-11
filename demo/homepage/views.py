# Create your views here.
from django.shortcuts import render
from .models import Book

def home_page(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'index.html', {'books': books})

