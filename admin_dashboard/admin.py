from django.contrib import admin
<<<<<<< HEAD
from .models import Department, Allocation, Scheme, Announcement, Place, Population, Complaint

# Register your models here.
admin.site.register([Department, Allocation, Scheme, Announcement, Place, Population, Complaint])
=======
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
>>>>>>> 1b0ba044e93796d7d6828104798b7bc34c48f650
