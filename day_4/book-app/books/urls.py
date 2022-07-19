# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import AuthorViewSet, BookViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = router.urls

urlpatterns += [
  # path('', views.index, name='index'),
  # path('author/<int:author_id>', views.author, name='author'),
  # path('category/<int:category_id>', views.category, name='category')
]