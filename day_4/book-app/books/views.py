#Django Rest Framework
from rest_framework.views import Response
from rest_framework import viewsets

# models
from .models import Author, Category, Book

# serializers

from .serializers import BookSerializer, AuthorSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  

class AuthorViewSet(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer