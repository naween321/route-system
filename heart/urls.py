from django.urls import path
from .views import HomeView, BusView, RouteView, BusRoutesView, RouteBusesView


urlpatterns = [
    path("buses/", BusView.as_view(), name="buses"),
    path("buses/<int:id>/routes/", BusRoutesView.as_view(), name="bus_routes"),
    path("routes/", RouteView.as_view(), name="routes"),
    path("routes/<int:id>/buses/", RouteBusesView.as_view(), name="route_buses"),
    path("", HomeView.as_view(), name='home')
]
