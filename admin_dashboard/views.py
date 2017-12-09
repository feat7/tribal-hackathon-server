from django.shortcuts import render
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
