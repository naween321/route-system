from django.db.models import Subquery, OuterRef, Count
from django.views.generic import TemplateView, ListView
from django_tables2 import SingleTableView
from .models import Bus, BusRoute, Route
from .tables import BusTable, RouteTable


class HomeView(TemplateView):
    template_name = 'home.html'


class BusView(SingleTableView):
    template_name = 'bus.html'
    table_class = BusTable

    def get_queryset(self):
        return Bus.objects.all().annotate(number_of_routes_this_bus_runs_on=Subquery(BusRoute.objects.
                                                                                     filter(bus_id=OuterRef('id')).
                                                                                     values('bus').
                                                                                     annotate(count=Count('pk')).
                                                                                     values('count')))


class RouteView(SingleTableView):
    template_name = 'route.html'
    table_class = RouteTable

    def get_queryset(self):
        return Route.objects.all().annotate(buses_number=Subquery(BusRoute.objects.filter(route_id=OuterRef('id')).
                                                                  values('route').annotate(count=Count('pk')).
                                                                  values('count')))


class RouteBusesView(SingleTableView):pass
class BusRoutesView(SingleTableView):pass
