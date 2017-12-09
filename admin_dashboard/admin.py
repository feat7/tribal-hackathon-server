from django.contrib import admin
from .models import Scheme, Place, Population

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'description', 'type', 'upper_node')
    pass
admin.site.register(Place, PlaceAdmin)

class SchemeAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Scheme, SchemeAdmin)

class PopulationAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Population, PopulationAdmin)