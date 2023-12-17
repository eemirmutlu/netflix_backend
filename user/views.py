from django.shortcuts import render
from .forms import *

# Create your views here.

def login_view(request):


    return render(request, 'login.html', {})
