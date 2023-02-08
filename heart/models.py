from django.db import models


class Bus(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    buses = models.ManyToManyField(Bus, through='BusRoute')

    def __str__(self):
        return self.name


class BusRoute(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    def __str__(self):
        return f'{self.bus.name} --> {self.route.name}'
