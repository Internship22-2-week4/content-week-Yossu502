from django.test import TestCase
from .models import Category, Author, Book
# Create your tests here.

class CategoryModelTest(TestCase):
  """
  Test for category model
  """

  def setUp(self):
    """
    Configuration initial
    """
    Category.objects.create(name='test', description='test', status=True)

  
  def test_category_name_is_not_blank(self):
    """
    Test for category name is not blank
    """ 
    category = Category.objects.get(id=1)
    self.assertIsNot(category.name, '')