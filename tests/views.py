from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the tests index.")