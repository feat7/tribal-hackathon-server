from django.contrib import admin
from .models import Allocation, Scheme, Announcement, Place, Population, Complaint

# Register your models here.
admin.site.register([Allocation, Scheme, Announcement, Place, Population, Complaint])