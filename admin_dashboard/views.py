from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Allocation, Scheme, Place, Department, Announcement
from material.frontend.views import ModelViewSet, ListModelView
from . import models

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
                "department_name" : temp_department.name,
                "likes" : temp_scheme.likes,
                "dis_likes" : temp_scheme.dis_likes,
                "allocated_amount" : temp_scheme.allocated_amount,
                "used_amount" : temp_scheme.used_amount
            }

            scheme_list.append(temp_data)
            temp_data = {}

        data = {
            "success": True,
            "schemes": scheme_list
        }
        
        return JsonResponse(data, safe=False)

    def like(self, id):
        scheme = Scheme.objects.get(pk=id)
        scheme.likes = scheme.likes + 1
        scheme.save()

        data = {
            "success": True,
            "likes": scheme.likes,
            "dis_likes": scheme.dis_likes
        }

        return JsonResponse(data, safe=False)

    def dis_like(self, id):
        scheme = Scheme.objects.get(pk=id)
        scheme.dis_likes = scheme.dis_likes + 1
        scheme.save()

        data = {
            "success": True,
            "likes": scheme.likes,
            "dis_likes": scheme.dis_likes
        }

        return JsonResponse(data, safe=False)

    def view_all(request):
        return render(request, 'user/schemes.html')


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


class graphs():

    def normal(request, used, allocated):

        performance = (int(used)/int(allocated))*100; 
        other = 100-performance; 
        return render(request, 'graphs/normal.html', {'performance': performance, 'other': other});

class announcements():
    def all(self):
        temp_announcements = Announcement.objects.filter(status="YES")
        announcement_list = []
        temp_data = {}

        for temp_announcement in temp_announcements:
            temp_data = {
                "id": temp_announcement.id,
                "name": temp_announcement.name,
                "description": temp_announcement.description,
            }

            announcement_list.append(temp_data)
            temp_data = {}

        data = {
            "success": True,
            "announcements": announcement_list
        }
        
        return JsonResponse(data, safe=False)

    def like(self, id):
        announcement = announcement.objects.get(pk=id)
        announcement.likes = announcement.likes + 1
        announcement.save()

        data = {
            "success": True,
            "likes": announcement.likes,
            "dis_likes": announcement.dis_likes
        }

        return JsonResponse(data, safe=False)

    def dis_like(self, id):
        announcement = announcement.objects.get(pk=id)
        announcement.dis_likes = announcement.dis_likes + 1
        announcement.save()

        data = {
            "success": True,
            "likes": announcement.likes,
            "dis_likes": announcement.dis_likes
        }

        return JsonResponse(data, safe=False)