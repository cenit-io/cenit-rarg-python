from django.shortcuts import render
from django.http import HttpResponse
import json

response = None


def done(result):
  global response
  response = HttpResponse(json.dumps(result), content_type='application/json')


# Create your views here.
def index(request):
  if request.method == 'GET':
    return render(request, 'index.html')
  else:
    params = request.POST.get('parameters', {})
    if params == '': params = {}

    if type(params) == str or type(params) == unicode:
      scope = json.loads(params)
    else:
      scope = params

    scope['done'] = done

    exec (request.POST['code'], scope)
    return response
