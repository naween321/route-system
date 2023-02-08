from django.db.models import Subquery, OuterRef, Count
from django.views.generic import TemplateView, ListView
from django_tables2 import SingleTableView
from .models import Bus, BusRoute, Route
from .tables import BusTable, RouteTable, RouteBusesTable, BusRoutesTable


class HomeView(TemplateView):
    template_name = 'home.html'


class BusView(SingleTableView):
    template_name = 'table.html'
    table_class = BusTable

    def get_queryset(self):
        return Bus.objects.all().annotate(number_of_routes_this_bus_runs_on=Subquery(BusRoute.objects.
                                                                                     filter(bus_id=OuterRef('id')).
                                                                                     values('bus').
                                                                                     annotate(count=Count('pk')).
                                                                                     values('count')))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['table_title'] = "Buses"
        return context


class RouteView(SingleTableView):
    template_name = 'table.html'
    table_class = RouteTable

    def get_queryset(self):
        return Route.objects.all().annotate(buses_number=Subquery(BusRoute.objects.filter(route_id=OuterRef('id')).
                                                                  values('route').annotate(count=Count('pk')).
                                                                  values('count')))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['table_title'] = "Routes"
        return context


class RouteBusesView(SingleTableView):
    template_name = "table.html"
    table_class = RouteBusesTable

    def get_queryset(self):
        route_id = self.kwargs['id']
        return BusRoute.objects.filter(route_id=route_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        route_id = self.kwargs.get('id')
        try:
            route = Route.objects.get(id=route_id)
        except Route.DoesNotExist:
            return context
        context['table_title'] = f"Buses on Route {route.name}"
        return context


class BusRoutesView(SingleTableView):
    template_name = "table.html"
    table_class = BusRoutesTable

    def get_queryset(self):
        bus_id = self.kwargs['id']
        return BusRoute.objects.filter(bus_id=bus_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print(context)
        bus_id = self.kwargs.get('id')
        try:
            bus = Bus.objects.get(id=bus_id)
        except Route.DoesNotExist:
            return context
        context['table_title'] = f"Routes of the Bus {bus.name}"
        return context
