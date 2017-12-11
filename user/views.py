from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string	
from django.conf import settings

def index(request):
    return render(request, 'user/index.html')

def statistics(request):
    return render(request, 'user/statistics.html')