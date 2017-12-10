from django.contrib import admin
from .models import Department, Allocation, Scheme, Announcement, Place, Population, Complaint

# Register your models here.
admin.site.register([Department, Allocation, Scheme, Announcement, Place, Population, Complaint])
