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
                "department_id" : temp_department.id,
                "department_name" : temp_department.name
            }

            scheme_list.append(temp_data)
            temp_data = {}

        data = {
            "success": True,
            "schemes": scheme_list
        }
        
        return JsonResponse(data, safe=False)

class places():
    def all(self):
        temp_places = Place.objects.filter(status="NO")
        place_list = []
        temp_data = {}

        for temp_place in temp_places:
            temp_data = {
                "id": temp_place.id,
                "name": temp_place.name,
                "type": temp_place.type,
                "upper_node": temp_place.upper_node_id,
                "description": temp_place.description
            }
            place_list.append(temp_data)
            temp_data = {}

        data = {
            "success": True,
            "places": place_list
        }
        return JsonResponse(data, safe=False)
