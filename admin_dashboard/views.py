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
        all_schemes = Scheme.objects.all().values()
        data = {
            "success": True,
            "schemes": list(all_schemes),
        }
        return JsonResponse(data, safe=False)

class places():
    def all(self):
        all_places = Place.objects.all().values()
        data = {
            "success": True,
            "schemes": list(all_places)
        }
        return JsonResponse(data, safe=False)
