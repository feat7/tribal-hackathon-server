from django.shortcuts import render
from django.http import JsonResponse
from .models import Allocation, Scheme, Place, Department

# Create your views here.
class allocations():
    def all(self):
        all_allocations = Allocation.objects.all()
        return JsonResponse(list(all_allocations.values()), safe=False)

class schemes():
    def all(self):
        temp_schemes = Scheme.objects.filter(status="NO")
        scheme_list = []
        temp_data = {}
        temp_department = {}

        for temp_scheme in temp_schemes:
            temp_department = Department.objects.get(id=temp_scheme.department.id)

            temp_data = {
                "id": temp_scheme.id,
                "name": temp_scheme.name,
                "description": temp_scheme.description,
                "department": {
                    "id" : temp_department.id,
                    "name" : temp_department.name,
                    "description" : temp_department.description                    
                }
            }

            scheme_list.append(temp_data)
            temp_scheme = {}

        data = {
            "success": True,
            "schemes": scheme_list
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
