from django.shortcuts import render
from django.http import JsonResponse
from .models import Allocation, Scheme, Place

# Create your views here.
class allocations():
    def all(self):
        all_allocations = Allocation.objects.all()
        return JsonResponse(list(all_allocations.values()), safe=False)

class schemes():
    def all(self):
        all_schemes = Scheme.objects.all()
        return JsonResponse(list(all_schemes.values()), safe=False)

class places():
    def all(self):
        all_places = Place.objects.all()
        return JsonResponse(list(all_places.values()), safe=False)
