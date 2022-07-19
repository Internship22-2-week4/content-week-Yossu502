from django.http import HttpResponse
from datetime import datetime
import pdb
import json

def helloWorld(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse(f'Oh, Hi Current server time is {now}')


def sorted_numbers(request):
  number = request.GET['numbers']
  number = [int(i) for i in number.split(',')]
  sorted_ints = sorted(number)
  data = {
    'status': 'ok',
    'numbers': sorted_ints,
    'message': 'La lista se ordeno exitosamente'
  }
  return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
  """Return a greetting"""
  if age < 12:
    message = f'Sorry {name}, you are not allowed here'
  else:
    message = f'Hello {name}, welcome to platzigram'

  return HttpResponse(message)