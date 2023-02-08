from django.contrib import admin
from .models import Bus, Route, BusRoute

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(BusRoute)
