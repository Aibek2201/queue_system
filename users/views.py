from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def auth(request):
    response = render_to_string('users/home.html')
    return HttpResponse(response)
