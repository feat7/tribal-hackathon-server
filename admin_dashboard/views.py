from django.shortcuts import render
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

        used = 0
        allocated = 0

        for temp_allocation in temp_allocations:
            temp_data = {
                "id": temp_allocation.id,
                "allocated_amount": temp_allocation.allocated_amount,
                "used_amount": temp_allocation.used_amount,
                "scheme_name": temp_allocation.scheme.name,
            }
            used += temp_allocation.used_amount
            allocated += temp_allocation.allocated_amount

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
                "name": temp_level.name
            }
            level_list.append(temp_data)
            temp_data = {}
        


        data = {
            "success": True,
            "allocations": allocation_list,
            "sub_levels": level_list,
            "used_amount": used,
            "allocated_amount": allocated
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

<<<<<<< HEAD
def admin_panel(request):
    return render(request, 'admin_dashboard/index.html')
=======

class graphs():

    def normal(request, used, allocated):

        performance = (int(used)/int(allocated))*100; 
        other = 100-performance; 
        return render(request, 'graphs/normal.html', {'performance': performance, 'other': other});
>>>>>>> 2c9e901a5a22ee5c70238ffba3a0f5c0b8e4bb2d
