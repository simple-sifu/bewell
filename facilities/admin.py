from django.contrib import admin

# Register your models here.
from .models import HealthFacilities, Description, Location

admin.site.register(HealthFacilities)
admin.site.register(Description)
admin.site.register(Location)
