from django.contrib import admin
from . import models
from .models import Department, Allocation, Scheme, Announcement, Place, Population, Complaint

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_balance</i>'
    list_display = ('name', 'description', 'status')

@admin.register(models.Allocation)
class AllocationAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_balance</i>'
    list_display = ('scheme', 'place', 'description', 'allocated_amount', 'used_amount', 'status')

@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">announcement</i>'
    list_display = ('name', 'description', 'status')

@admin.register(models.Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">forum</i>'
    list_display = ('id', 'name', 'description', 'allocation', 'status', 'created_at')

@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    icons = '<i class="material-icons">place</i>'
    list_display = ('name', 'description', 'type', 'upper_node', 'population', 'status')

@admin.register(models.Population)
class PopulationAdmin(admin.ModelAdmin):
    icons = '<i class="material-icons">people</i>'
    list_display = ('id', 'total_population', 'tribal_population', 'tribal_population_percent', 'status')

@admin.register(models.Scheme)
class SchemeAdmin(admin.ModelAdmin):
    icons = '<i class="material-icons">assignment</i>'
    list_display = ('name', 'department', 'description', 'allocated_amount', 'used_amount', 'likes', 'dis_likes', 'status', 'updated_at')