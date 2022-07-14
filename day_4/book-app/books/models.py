from django.db import models

# Create your models here.

class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  image = models.CharField(max_length=100)
  status = models.BooleanField(default=True)

  def __str__(self) -> str:
    return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
  """
  Category model.
  Requires a name, description and status
  
  """
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  status = models.BooleanField(default=True)

  def __str__(self) -> str:
    return f'{self.name} -- {self.description} -- {self.status}'


class Book(models.Model):
  """
  Book Model
  Requires title, image, isbn, status, idAuthor, idCategory

  """
  title = models.CharField(max_length=50)
  image = models.CharField(max_length=200)
  isb = models.CharField(max_length=20)
  status = models.BooleanField(default=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.title} - {self.isb} - {self.author.first_name}'

