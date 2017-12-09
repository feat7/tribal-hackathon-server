from django.shortcuts import render
from .models import Place, Complaint
from django.http import JsonResponse

# Create your views here.
class places():

    def all(self):
        all_places = Place.objects.all()
        return JsonResponse(all_places, safe=False)

class complaints():

    def all(self):
        all_complaints = Complaint.objects.all()
        return JsonResponse(all_complaints, safe=False)