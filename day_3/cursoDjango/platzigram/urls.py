from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('helloWorld/', local_views.helloWorld),
    path('sorted/', local_views.sorted_numbers),
    path('hi/<str:name>/<int:age>', local_views.say_hi),
    path('posts/', posts_views.list_posts),
    path('admin/', admin.site.urls)
]
