from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string	
from django.conf import settings

def index(request):
    print (settings.STATIC_ROOT)
    print (settings.STATICFILES_DIRS)
    return render(request, 'user/index.html')