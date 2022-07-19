import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


posts = [
    {
        'title': 'Mont Blac',
        'user':{
          'name': 'Cristhan V.',
          'picture': 'https://picsum.photos/60/60/?image=250'
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title': 'Via LActeria',
        'user':{
          'name': 'Lucas Jorge V.',
          'picture': 'https://picsum.photos/60/60/?image=251'
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'title': 'Guatemala',
        'user':{
          'name': 'Josue David M.',
          'picture': 'https://picsum.photos/60/60/?image=252'
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=502',
    },
    
]

def list_posts(request):
  content = []
  return render(request, 'feed.html', {
    'posts': posts
  })
