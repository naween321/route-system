import django_tables2 as tables
from django_tables2.utils import A
from .models import Bus, Route, BusRoute


class BusTable(tables.Table):
    number_of_routes_this_bus_runs_on = tables.LinkColumn("bus_routes", args=[A("pk")])

    class Meta:
        model = Bus
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "number", "number_of_routes_this_bus_runs_on")


class RouteTable(tables.Table):
    buses_number = tables.LinkColumn("route_buses", args=[A("pk")])

    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "number", "buses_number")


class RouteBusesTable(tables.Table):
    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("bus__name", "bus__number", "from_time", "to_time")


class BusRoutesTable(tables.Table):
    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("route__name", "route__number", "from_time", "to_time")
