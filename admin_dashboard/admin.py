from django.contrib import admin
<<<<<<< HEAD
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
=======
from .models import Allocation, Scheme, Announcement, Place, Population, Complaint

# Register your models here.
admin.site.register([Allocation, Scheme, Announcement, Place, Population, Complaint])
>>>>>>> e57db530567cdb320f654cb648f037a9ff2db87f
