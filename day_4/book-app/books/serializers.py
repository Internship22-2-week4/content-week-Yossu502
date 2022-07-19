#Django rest framework serializers
from rest_framework import serializers

#models
from .models import Book, Author, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
  # Metodo para mostrar datos de relacion entre tablas
  # author = AuthorSerializer()
  # category = CategorySerializer()

  # Metodo 2 para mostrar datos de realcion entre tablas
  # category = serializers.SlugRelatedField(
  #   many=False,
  #   read_only=True,
  #   slug_field='name'
  # )
  # author = serializers.SlugRelatedField(
  #   many=False,
  #   read_only=True,
  #   slug_field='first_name'
  # )

  # Metodo 3 para mostrar datos de relacion entre tablas
  # author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
  # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
  class Meta:
    model = Book
    fields = '__all__'
    # fields = ['title', 'author', 'category']
  
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'title': instance.title,
      'image': instance.image,
      'isbn': instance.isb,
      'author': instance.author.first_name + " " + instance.author.last_name,
      'category': instance.category.name
    }