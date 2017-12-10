from django.shortcuts import render
<<<<<<< HEAD
from django.http import JsonResponse, HttpResponse
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

    def search(self, id):
        temp_allocations = Allocation.objects.filter(place_id=id)
        allocation_list = []
        temp_data = {}

        for temp_allocation in temp_allocations:
            temp_data = {
                "id": temp_allocation.id,
                "allocated_amount": temp_allocation.allocated_amount,
                "used_amount": temp_allocation.used_amount,
                "scheme_name": temp_allocation.scheme.name,
            }
            allocation_list.append(temp_data)
            temp_data = {}

        temp_levels = Place.objects.filter(upper_node_id=id)
        level_list = []
        temp_data = {}

        for temp_level in temp_levels:
            temp_data = {
                "id": temp_level.id,
                "name": temp_level.name,
                "description": temp_level.description,
                "name": temp_level.name,
            }
            level_list.append(temp_data)
            temp_data = {}
        


        data = {
            "success": True,
            "allocations": allocation_list,
            "sub_levels": level_list
        }

        return JsonResponse(data, safe=False)

class departments():

    def all(self):
        all_departments = Department.objects.all().values()

        data = {
            "success": True,
            "departments": list(all_departments)
        }

        return JsonResponse(data, safe=False)
=======
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Place

# Create your views here.
def list_all_places(request):
    temp_places = Place.objects.filter(status="YES")
    place_list = []
    temp_data = {}
    for temp_place in temp_places:
        temp_data = {
            "id" : temp_place.id,
            "name" : temp_place.name,
            "description" : temp_place.description,
            "type" : temp_place.type
        }
        place_list.append(temp_data)
        temp_place = {}
    json_data = {
        "success" : True,
        "places" : place_list
    }    
    return JsonResponse(json_data, safe=False)
>>>>>>> 1b0ba044e93796d7d6828104798b7bc34c48f650
