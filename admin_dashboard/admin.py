from django.contrib import admin
from .models import Scheme, Place, Population, Complaint

# Register your models here.
admin.site.register([Scheme, Place, Population, Complaint])