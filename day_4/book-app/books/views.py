from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Category, Book

# Create your views here.

def index(request):
  # return HttpResponse('App Books')
  books = Book.objects.all()
  return render(request, 'books/index.html', {
    "books_list": books
  })


def author(request, author_id):
  author = Author.objects.get(id=author_id)
  return render(request, 'books/author.html', {
    "author": author
  })
  # return HttpResponse(f'Author id: {author_id}')


def category(request, category_id):
  return HttpResponse(f'Category id: {category_id}')