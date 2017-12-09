from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string	

def index(request):
    return render(request, 'user/index.html')